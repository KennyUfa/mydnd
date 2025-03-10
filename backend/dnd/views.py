import math
import random

from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets, permissions, status, generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import *

class CharacterCustomAbilityUpdateView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = AbilitySerializer
    def patch(self, request, pk):

        ability = get_object_or_404(CustomAbility, pk=pk)
        ability.custom_description = request.data.get('custom_description')
        ability.save()
        return Response(CustomAbilitySerializer(ability).data)

        # if not custom_ability_id:

class BaseClassChViewSet(generics.ListAPIView):
    queryset = BaseClass.objects.all()
    serializer_class = BaseClassListSerializer
    permission_classes = [permissions.IsAuthenticated]


class RaceListView(generics.ListAPIView):
    queryset = Race.objects.all()
    serializer_class = RaceListSerializer
    permission_classes = [permissions.IsAuthenticated]


class OriginListView(generics.ListAPIView):
    queryset = OriginModel.objects.all()
    serializer_class = OriginListSerializer
    permission_classes = [permissions.IsAuthenticated]


class CharacterOriginView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def patch(self, request, character_id):
        # Получаем персонажа по id
        character = get_object_or_404(Character, id=character_id)

        # Получаем ID предыстории из данных запроса
        origin_id = request.data.get('id')
        if not origin_id:
            return Response({'error': 'origin_id is required'},
                            status=status.HTTP_400_BAD_REQUEST)

        # Получаем объект предыстории
        origin = get_object_or_404(OriginModel, id=origin_id)

        # Привязываем предысторию к персонажу
        character.origin = origin
        character.save()

        # Возвращаем сериализованные данные персонажа
        serializer = Origin(character.origin)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CharacterHideOriginalAbilityView(APIView):
    """Обновления описания способностей класса персонажа"""
    permission_classes = [permissions.IsAuthenticated]

    def patch(self, request, pk):
        character = get_object_or_404(Character, pk=pk)
        print(request.data)
        original_ability_id = request.data.get('id')
        custom_ability = CustomAbility.objects.filter(ability=original_ability_id, character=character).first()
        print(custom_ability)
        if custom_ability:
            print("Есть custom_ability_id")
        # Если custom_ability_id не передан, то создаем новую запись в CustomAbility с hide_original=True
        if not custom_ability:
            print("Нет custom_ability_id")
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
            custom_ability_id = CustomAbility.objects.create(character=character, ability=original_ability, hide_original=True, hide_custom=True,
                                                             custom_description=f"Своё описание способности: {original_ability.description}")
        custom_ability_id.hide_custom = not custom_ability_id.hide_custom
        custom_ability_id.save()
        serializer = CustomAbilityPatchSerializer(custom_ability_id)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CharacterWorldOutlookView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def patch(self, request, character_id):
        # Получаем персонажа по id
        character = get_object_or_404(Character, id=character_id)

        # Получаем ID мировоззрения из данных запроса
        world_outlook_id = request.data.get('id')
        if not world_outlook_id:
            return Response({'error': 'id is required'},
                            status=status.HTTP_400_BAD_REQUEST)

        # Получаем объект предыстории
        world_outlook = get_object_or_404(WorldOutlook, id=world_outlook_id)

        # Привязываем предысторию к персонажу
        character.world_outlook = world_outlook
        character.save()

        # Возвращаем сериализованные данные персонажа
        serializer = WorldOutlookSerializer(character.world_outlook)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CharacterDeleteView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CharacterSerializer

    def delete(self, request, pk):
        character = get_object_or_404(Character, pk=pk)
        character.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CharacterDetailView(APIView):
    """Получение информации о персонаже."""

    def get(self, request, pk):
        try:
            character = Character.objects.get(pk=pk)
        except Character.DoesNotExist:
            return Response({"error": "Character not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = CharacterSerializer(character, context={'character': character})
        return Response(serializer.data)

    def patch(self, request, pk):
        character = get_object_or_404(Character, pk=pk)
        serializer = CharacterSerializer(character, context={'character': character}, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CharacterListView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CharacterSerializerList

    def get(self, request):
        queryset = Character.objects.filter(account=self.request.user)
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        print('post')
        serializer_class = CreateCharacterSerializer(data=request.data)
        if serializer_class.is_valid():
            print('post valid')
            data = serializer_class.save(account=self.request.user)
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)


class CharacterCreateView(APIView):
    def post(self, request):
        serializer = CreateCharacterSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(account=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SpellView(viewsets.ReadOnlyModelViewSet):
    queryset = Spell.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter,
                       DjangoFilterBackend]
    serializer_class = SpellBookSerializer

    def retrieve(self, request, pk=None):
        spell = get_object_or_404(Spell, pk=pk)
        serializer = ChampionSpellSerializer(spell)
        return Response(serializer.data)

    def get_queryset(self):
        search_query = self.request.query_params.get('search', '')
        queryset = Spell.objects.all()

        if search_query:
            queryset = queryset.filter(name__iregex=search_query.strip())
        return queryset


class ProtectStateView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProtectStateSerializer
    queryset = ProtectStateModel.objects.all()


class SkillStateView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = SkillStateSerializer
    queryset = SkillStateModel.objects.all()


class WorldOutlookView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = WorldOutlook.objects.all()
    serializer_class = WorldOutlookSerializer

    def get_queryset(self):
        return WorldOutlook.objects.all()


class ItemView(viewsets.ReadOnlyModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Item.objects.all()
    filter_backends = [filters.SearchFilter, filters.OrderingFilter,
                       DjangoFilterBackend]
    serializer_class = ItemsSerializer

    def retrieve(self, request, pk=None):
        item = get_object_or_404(Item, pk=pk)
        serializer = ItemsSerializer(item)
        return Response(serializer.data)

    def get_queryset(self):
        search_query = self.request.query_params.get('search', '')
        queryset = Item.objects.all()
        if search_query:
            queryset = queryset.filter(name__iregex=search_query)
        return queryset


class InventoryItemView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, character_id):
        character = get_object_or_404(Character, id=character_id)
        item_id = request.data.get('item_id')
        quantity = request.data.get('quantity', 1)
        item = get_object_or_404(Item, id=item_id)
        inventory_item, created = InventoryItem.objects.get_or_create(
            character=character, item=item)
        if not created:
            inventory_item.quantity = quantity
        else:
            inventory_item.quantity = quantity
        inventory_item.save()
        serializer = InventorySerializer(inventory_item)
        return Response(serializer.data)

    def delete(self, request, character_id):
        character = get_object_or_404(Character, id=character_id)
        item_id = request.data.get('item_id')
        item = get_object_or_404(Item, id=item_id)
        inventory_item = get_object_or_404(InventoryItem,
                                           character=character, item=item)
        inventory_item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self, request, character_id):
        character = get_object_or_404(Character, id=character_id)
        for item in request.data.get('my_items'):
            item_id = int(item.get('item').get("id"))
            quantity = int(item.get('quantity'))
            inventory_item = get_object_or_404(InventoryItem,
                                               character=character,
                                               item__id=item_id)
            inventory_item.quantity = quantity
            if quantity <= 0:
                inventory_item.delete()
            else:
                inventory_item.save()
        inventory = character.my_items.all()
        serializer = InventorySerializer(inventory, many=True)
        return Response(serializer.data)


class RandomSaveView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        print(request.data)

        character = Character.objects.get(id=request.data.get('championId'))
        skillvalue = getattr(character, request.data.get('statValue'))
        if 'protectValueName' in request.data:
            protect_state = getattr(character.protect_state,
                                    request.data.get('protectValueName'))
            possession_bonus = character.possession_bonus
            result = math.floor((skillvalue - 10) / 2)
            random_result = random.randint(1, 20)

            match protect_state:
                case 1:
                    resp = {
                        'total': random_result + result,
                        'skillValue': skillvalue,
                        'random_result': random_result,
                        'possession_bonus': possession_bonus,
                    }
                    return Response(resp)
                case 2:
                    resp = {
                        'total': random_result + result + possession_bonus,
                        'skillValue': skillvalue,
                        'random_result': random_result,
                        'possession_bonus': possession_bonus,
                    }
                    return Response(resp)
                case _:
                    return Response(status=status.HTTP_400_BAD_REQUEST)
        elif 'abilityValueName' in request.data:
            abilityValueName = getattr(character.skill_state,
                                       request.data.get('abilityValueName'))
            possession_bonus = character.possession_bonus
            result = math.floor((skillvalue - 10) / 2)
            random_result = random.randint(1, 20)

            match abilityValueName:
                case 1:
                    resp = {
                        'total': random_result + result,
                        'skillValue': skillvalue,
                        'random_result': random_result,
                        'possession_bonus': possession_bonus,
                    }
                    print('1')
                    return Response(resp)
                case 2:
                    print('2')
                    resp = {
                        'total': random_result + result + possession_bonus,
                        'skillValue': skillvalue,
                        'random_result': random_result,
                        'possession_bonus': possession_bonus,
                    }
                    return Response(resp)
                case _:
                    return Response(status=status.HTTP_400_BAD_REQUEST)
