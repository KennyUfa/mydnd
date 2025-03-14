import math
import random

from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets, permissions, status, generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .db.background import SelectedFeatureOption, FeatureOption, Feature, Flaw, SelectedOrigin, Bond, Trait, Ideal
from .serializers.background_serializers import BackgroundListSerializer, SelectedOriginSerializer
from .serializers.serializers import *


class CharacterProtectStateView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProtectStateSerializer

    def patch(self, request, pk):
        # Получаем объект Character
        character = get_object_or_404(Character, pk=pk)

        # Проверяем права доступа
        if character.account != request.user:
            return Response({"error": "You do not have permission to edit this character."}, status=403)

        # Получаем данные skill_state из запроса
        print(request.data)
        protect_state_data = request.data.get('protect_state', {})
        protect_state_id = protect_state_data.pop('id', None)

        try:
            # Обновляем существующий объект или создаем новый
            protect_state, created = ProtectStateModel.objects.update_or_create(
                id=protect_state_id,
                defaults=protect_state_data
            )
        except Exception as e:
            return Response({"error": f"Failed to update skill state: {str(e)}"}, status=400)

        # Присваиваем объект character.skill_state
        character.protect_state = protect_state
        character.save()

        # Возвращаем сериализованные данные
        return Response(ProtectStateSerializer(protect_state).data)


class CharacterSkillStateView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = SkillStateSerializer

    def patch(self, request, pk):
        # Получаем объект Character
        character = get_object_or_404(Character, pk=pk)

        # Проверяем права доступа
        if character.account != request.user:
            return Response({"error": "You do not have permission to edit this character."}, status=403)

        # Получаем данные skill_state из запроса
        skill_state_data = request.data.get('skill_state', {})
        skill_state_id = skill_state_data.pop('id', None)

        try:
            # Обновляем существующий объект или создаем новый
            skill_state, created = SkillStateModel.objects.update_or_create(
                id=skill_state_id,
                defaults=skill_state_data
            )
        except Exception as e:
            return Response({"error": f"Failed to update skill state: {str(e)}"}, status=400)

        # Присваиваем объект character.skill_state
        character.skill_state = skill_state
        character.save()

        # Возвращаем сериализованные данные
        return Response(SkillStateSerializer(skill_state).data)


class CharacterSkillsView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = SkillsSerializer

    def patch(self, request, pk):
        character = get_object_or_404(Character, pk=pk)
        if character.skills:
            # Обновляем значения существующего объекта
            character.skills.strength = request.data.get('strength')
            character.skills.dexterity = request.data.get('dexterity')
            character.skills.constitution = request.data.get('constitution')
            character.skills.intelligence = request.data.get('intelligence')
            character.skills.wisdom = request.data.get('wisdom')
            character.skills.charisma = request.data.get('charisma')
            character.skills.save()
        return Response(SkillsSerializer(character.skills).data)


class CharacterCustomAbilityUpdateView(APIView):
    """ Update a custom ability"""
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


class BackgroundListView(generics.ListAPIView):
    queryset = Background.objects.all()
    serializer_class = BackgroundListSerializer
    permission_classes = [permissions.IsAuthenticated]


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
            return Response({"error": "You do not have permission to edit this character."}, status=403)
        else:
            archetype = request.data.get('id')
            change_archetype = get_object_or_404(Archetype, id=archetype)
            character.archetype = change_archetype
            character.save()
            return Response(ArchetypeSerializer(character.archetype, context={'character': character}).data)


class SubRaceChangeView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def patch(self, request, pk):
        character = get_object_or_404(Character, pk=pk)
        if character.account != request.user:
            return Response({"error": "You do not have permission to edit this character."}, status=403)
        else:

            sub_race_id = request.data.get('id')
            change_sub_race = get_object_or_404(SubRace, id=sub_race_id)
            character.sub_race = change_sub_race
            character.save()
            return Response(SubRaceSerializer(character.sub_race, context={'character': character}).data)


class BackgroundChangeView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def patch(self, request, pk):
        character = get_object_or_404(Character, pk=pk)
        if character.account != request.user:
            return Response({"error": "You do not have permission to edit this character."}, status=403)
        else:

            background_id = request.data.get('id')
            change = get_object_or_404(Background, id=background_id)
            character.background = change
            character.save()
            return Response(BackgroundSerializer(character.background, context={'character': character}).data)


class BackgroundChangeOptionsView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def patch(self, request, pk):
        character = get_object_or_404(Character, pk=pk)
        option = get_object_or_404(FeatureOption, id=request.data.get('option'))
        feature = get_object_or_404(Feature, id=request.data.get('feature'))
        existing_option = SelectedFeatureOption.objects.filter(character=character, feature=feature).first()
        if existing_option:
            # Обновляем существующую запись
            existing_option.option = option
            existing_option.save()
            return Response(BackgroundSerializer(character.background, context={'character': character}).data)

        # Создаем новую запись
        new_option = SelectedFeatureOption.objects.create(
            character=character,
            feature=feature,
            option=option
        )
        return Response(BackgroundSerializer(character.background, context={'character': character}).data)


class BackgroundChangeOriginView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def patch(self, request, pk):
        character = get_object_or_404(Character, pk=pk)
        if request.data.get('flaw'):
            flaw = Flaw.objects.get(id=request.data.get('flaw').get('id'))
            character_selected_origin_options = SelectedOrigin.objects.get(character=character)
            character_selected_origin_options.flaw = flaw
            character_selected_origin_options.save()
            return Response(SelectedOriginSerializer(character_selected_origin_options).data)
        if request.data.get('bond'):
            bond = Bond.objects.get(id=request.data.get('bond').get('id'))
            character_selected_origin_options = SelectedOrigin.objects.get(character=character)
            character_selected_origin_options.bond = bond
            character_selected_origin_options.save()
            return Response(SelectedOriginSerializer(character_selected_origin_options).data)
        if request.data.get('trait'):
            trait = Trait.objects.get(id=request.data.get('trait').get('id'))
            character_selected_origin_options = SelectedOrigin.objects.get(character=character)
            character_selected_origin_options.trait = trait
            character_selected_origin_options.save()
            return Response(SelectedOriginSerializer(character_selected_origin_options).data)
        if request.data.get('ideal'):
            ideal = Ideal.objects.get(id=request.data.get('ideal').get('id'))
            character_selected_origin_options = SelectedOrigin.objects.get(character=character)
            character_selected_origin_options.ideal = ideal
            character_selected_origin_options.save()
            return Response(SelectedOriginSerializer(character_selected_origin_options).data)


class RaceListView(generics.ListAPIView):
    queryset = Race.objects.all()
    serializer_class = RaceListSerializer
    permission_classes = [permissions.IsAuthenticated]


class SubRaceListView(generics.ListAPIView):
    serializer_class = SubRaceSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        return SubRace.objects.filter(race=pk)


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
            custom_ability_id = CustomAbility.objects.create(character=character, ability=original_ability, hide_original=True,
                                                             hide_custom=True,
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
        skillvalue = getattr(character.skills, request.data.get('statValue'))
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
                    return Response(resp)
                case 2:
                    resp = {
                        'total': random_result + result + possession_bonus,
                        'skillValue': skillvalue,
                        'random_result': random_result,
                        'possession_bonus': possession_bonus,
                    }
                    return Response(resp)
                case 3:
                    resp = {
                        'total': random_result + result + possession_bonus + possession_bonus,
                        'skillValue': skillvalue,
                        'random_result': random_result,
                        'possession_bonus': possession_bonus,
                    }
                    return Response(resp)
