from django.db.models import Q
from rest_framework import generics, permissions, status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from champion_class.models import BaseClass, Archetype, CustomAbility, Ability
from champion_class.serializers import BaseClassListSerializer, AbilitySerializer, ArchetypeListSerializer, CustomAbilitySerializer, \
    ArchetypeSerializer, CustomAbilityPatchSerializer
from character.models import Character


class BaseClassChViewSet(generics.ListAPIView):
    queryset = BaseClass.objects.all()
    serializer_class = BaseClassListSerializer
    permission_classes = [permissions.IsAuthenticated]


class Archetypes(APIView):
    def get(self, request):
        class_names = request.query_params.getlist('class_actor[]', [])
        query = Q()
        queryset = Archetype.objects.all()
        if class_names:
            for class_name in class_names:
                query |= Q(character_class__id=class_name)

        queryset = queryset.filter(query)
        return Response(ArchetypeListSerializer(queryset, many=True).data)


class CharacterCustomAbilityUpdateView(APIView):
    """ Update a custom ability"""
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = AbilitySerializer

    def patch(self, request, pk):
        ability = get_object_or_404(CustomAbility, pk=pk)
        ability.custom_description = request.data.get('custom_description')
        ability.save()
        return Response(CustomAbilitySerializer(ability).data)


class ArchetypeViewSet(generics.ListAPIView):
    serializer_class = ArchetypeListSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        # Фильтруем и сортируем queryset
        return Archetype.objects.filter(character_class=pk)


class ArchetypeChangeView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def patch(self, request, pk):
        character = get_object_or_404(Character, pk=pk)
        if character.account != request.user:
            return Response({"error": "ArchetypeChangeView patch"}, status=403)
        else:
            archetype = request.data.get('id')
            change_archetype = get_object_or_404(Archetype, id=archetype)
            character.archetype = change_archetype
            character.save()
            return Response(ArchetypeSerializer(character.archetype, context={'character': character}).data)

    def delete(self, request, pk):
        character = get_object_or_404(Character, pk=pk)
        if character.account != request.user:
            return Response({"error": "ArchetypeChangeView delete"}, status=403)
        else:
            character.archetype = None
            character.save()
            return Response(status=status.HTTP_200_OK)


class CharacterHideOriginalAbilityView(APIView):
    """Обновления описания способностей класса персонажа"""
    permission_classes = [permissions.IsAuthenticated]

    def patch(self, request, pk):
        character = get_object_or_404(Character, pk=pk)
        original_ability_id = request.data.get('id')
        custom_ability = CustomAbility.objects.filter(ability=original_ability_id, character=character).first()

        if not custom_ability:
            original_ability = Ability.objects.filter(id=original_ability_id).first()
            custom_ability = CustomAbility.objects.create(character=character, ability=original_ability, hide_original=False,
                                                          hide_custom=request.data.get('custom_description').get('hide_custom'),
                                                          custom_description=f"Своё описание способности: {original_ability.description}")
            # Изменяем hide_original
        custom_ability.hide_original = not custom_ability.hide_original
        custom_ability.save()
        serializer = CustomAbilityPatchSerializer(custom_ability)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CharacterHideCustomAbilityView(APIView):
    """Обновления описания способностей класса персонажа"""
    permission_classes = [permissions.IsAuthenticated]

    def patch(self, request, pk):
        character = get_object_or_404(Character, pk=pk)
        original_ability_id = request.data.get('id')
        custom_ability_id = CustomAbility.objects.filter(ability=original_ability_id, character=character).first()
        if not custom_ability_id:
            original_ability = Ability.objects.filter(id=original_ability_id).first()
            custom_ability_id = CustomAbility.objects.create(character=character, ability=original_ability, hide_original=True,
                                                             hide_custom=True,
                                                             custom_description=f"Своё описание способности: {original_ability.description}")
        custom_ability_id.hide_custom = not custom_ability_id.hide_custom
        custom_ability_id.save()
        serializer = CustomAbilityPatchSerializer(custom_ability_id)
        return Response(serializer.data, status=status.HTTP_200_OK)
