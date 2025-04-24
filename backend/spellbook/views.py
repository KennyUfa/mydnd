from collections import defaultdict


from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions, filters
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from character.models import Character
from spellbook.models import Spell,CharacterSpellSlotLevel
from spellbook.serializers import SpellSerializer, SpellSlotLevelSerializer, CharacterSpellSlotLevelSerializer


class SpellView(viewsets.ReadOnlyModelViewSet):
    queryset = Spell.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter,
                       DjangoFilterBackend]
    serializer_class = SpellSerializer

    def retrieve(self, request, pk=None):
        spell = get_object_or_404(Spell, pk=pk)
        serializer = SpellSerializer(spell)
        return Response(serializer.data)

    def get_queryset(self):
        search_query = self.request.query_params.get('search', '')
        queryset = Spell.objects.all()

        if search_query:
            queryset = queryset.filter(name__iregex=search_query.strip())
        return queryset


class SpellBookSlotPatch(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def patch(self, request, character_id):
        character = get_object_or_404(Character, id=character_id)
        slot_data = request.data.get('level_slots')
        level = slot_data.get('level')
        count = slot_data.get('count')
        used = slot_data.get('used')
        change_level_slot = character.spell_slots.levels.get(level=level)
        change_level_slot.count = count
        change_level_slot.used = used
        change_level_slot.save()

        return Response(SpellSlotLevelSerializer(change_level_slot).data)


class SpellBookPatch(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def patch(self, request, character_id):
        character = get_object_or_404(Character, id=character_id)
        level_slot = character.spell_slots.levels.get(level=request.data['level_slots'])
        spell = get_object_or_404(Spell, id=request.data['spell'])
        spell_book = get_object_or_404(CharacterSpellSlotLevel, spell_slot_level=level_slot, character_spell_slots=character.spell_slots)
        spell_book.spells.append(spell.id)
        spell_book.save()
        return Response(CharacterSpellSlotLevelSerializer(spell_book).data)

    def delete(self, request, character_id):
        character = get_object_or_404(Character, id=character_id)
        level_slot = character.spell_slots.levels.get(level=request.query_params.get('level_slots[level]'))
        spell_book = get_object_or_404(CharacterSpellSlotLevel, spell_slot_level=level_slot)
        spell_book.spells.pop(int(request.query_params.get('spell_index')))
        spell_book.save()
        return Response(CharacterSpellSlotLevelSerializer(spell_book).data)


class SpellSearchView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):

        # Получаем параметры из запроса
        class_names = request.query_params.getlist('class_actor[]', [])
        archetype = request.query_params.getlist('archetype[]', [])
        search_query = request.query_params.get('search', '').strip()

        # Начинаем с базового запроса
        queryset = Spell.objects.all()

        # Создаем Q-объект для хранения всех условий
        query = Q()

        # Фильтрация по классам
        if class_names:
            for class_name in class_names:
                query |= Q(class_actor__id=class_name)
        if archetype:
            for arh in archetype:
                query |= Q(archetype__id=arh)

        # Поиск по названию или описанию
        if search_query:
            query &= Q(name__icontains=search_query) | Q(instruction__icontains=search_query)

        # применяем фильтры и группируем результаты
        queryset = queryset.filter(query).distinct()

        grouped_spells = defaultdict(list)
        for spell in queryset:
            serializer = SpellSerializer(spell)
            grouped_spells[spell.level].append(serializer.data)

        return Response(dict(grouped_spells))
