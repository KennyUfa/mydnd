import math
import random

from django.db.models import Q
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets, permissions, status, generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .db.background import SelectedFeatureOption, FeatureOption, Feature, Flaw, SelectedOrigin, Bond, Trait, Ideal
from .serializers.background_serializers import BackgroundListSerializer, SelectedOriginSerializer, SelectedFeatureOptionSerializer
from .serializers.serializers import *


# from dnd.serializers.temp.spellbook import CharacterSpellSlotLevelSerializer, SpellSlotLevelSerializer, SpellSerializer


class PossessionBonus(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def patch(self, request, character_id):
        character = get_object_or_404(Character, pk=character_id)
        character.possession_bonus = request.data.get('possession_bonus')
        character.save()
        return Response(status.HTTP_200_OK)


class Speed(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def patch(self, request, character_id):
        character = get_object_or_404(Character, pk=character_id)
        character.speed = request.data.get('speed')
        character.save()
        return Response(status.HTTP_200_OK)


class ProtectionClass(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def patch(self, request, character_id):
        character = get_object_or_404(Character, pk=character_id)
        character.protection_class = request.data.get('protection_class')
        character.save()
        return Response(status.HTTP_200_OK)


class InspirationBonus(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def patch(self, request, character_id):
        character = get_object_or_404(Character, pk=character_id)
        character.inspiration = request.data.get('inspiration')
        character.save()
        return Response(status.HTTP_200_OK)


class CharacterProtectStateView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProtectStateSerializer

    def patch(self, request, pk):
        # Получаем объект Character
        character = get_object_or_404(Character, pk=pk)
        # Проверяем права доступа
        if character.account != request.user:
            return Response({"error": "CharacterProtectStateView"}, status=403)
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
            return Response({"error": f" {str(e)}"}, status=400)

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
            return Response({"error": "CharacterSkillStateView"}, status=403)

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
            return Response({"error": f" {str(e)}"}, status=400)

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


class BackgroundListView(generics.ListAPIView):
    queryset = Background.objects.all()
    serializer_class = BackgroundListSerializer
    permission_classes = [permissions.IsAuthenticated]


class BackgroundChangeView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def patch(self, request, pk):
        character = get_object_or_404(Character, pk=pk)
        if character.account != request.user:
            return Response({"error": "BackgroundChangeView"}, status=403)
        else:
            background_id = request.data.get('id')
            change = get_object_or_404(Background, id=background_id)

            if hasattr(character.background, 'id') and character.background.id != background_id:
                character_selected_origin_options, _ = SelectedOrigin.objects.get_or_create(character=character)
                character_selected_origin_options.bond = None
                character_selected_origin_options.flaw = None
                character_selected_origin_options.ideal = None
                character_selected_origin_options.trait = None
                character_selected_origin_options.save()
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
            return Response(SelectedFeatureOptionSerializer(existing_option).data)
        else:

            # Создаем новую запись

            res = SelectedFeatureOption.objects.create(
                character=character,
                feature=feature,
                option=option
            )
            return Response(SelectedFeatureOptionSerializer(res).data)


class BackgroundChangeOriginView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def patch(self, request, pk):
        character = get_object_or_404(Character, pk=pk)
        if request.data.get('flaw'):
            flaw = Flaw.objects.get(id=request.data.get('flaw').get('id'))
            character_selected_origin_options, _ = SelectedOrigin.objects.get_or_create(character=character)
            character_selected_origin_options.flaw = flaw
            character_selected_origin_options.save()
            return Response(SelectedOriginSerializer(character_selected_origin_options).data)
        if request.data.get('bond'):
            bond = Bond.objects.get(id=request.data.get('bond').get('id'))
            character_selected_origin_options, _ = SelectedOrigin.objects.get_or_create(character=character)
            character_selected_origin_options.bond = bond
            character_selected_origin_options.save()
            return Response(SelectedOriginSerializer(character_selected_origin_options).data)
        if request.data.get('trait'):
            trait = Trait.objects.get(id=request.data.get('trait').get('id'))
            character_selected_origin_options, _ = SelectedOrigin.objects.get_or_create(character=character)
            character_selected_origin_options.trait = trait
            character_selected_origin_options.save()
            return Response(SelectedOriginSerializer(character_selected_origin_options).data)
        if request.data.get('ideal'):
            ideal = Ideal.objects.get(id=request.data.get('ideal').get('id'))
            character_selected_origin_options, _ = SelectedOrigin.objects.get_or_create(character=character)
            character_selected_origin_options.ideal = ideal
            character_selected_origin_options.save()
            return Response(SelectedOriginSerializer(character_selected_origin_options).data)


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
        serializer_class = CreateCharacterSerializer(data=request.data)
        if serializer_class.is_valid():
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


class MaxHitView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def patch(self, request, character_id):
        character = get_object_or_404(Character, pk=character_id)
        character.max_hit = request.data.get('max_hit')
        tmp = request.data.get('temp_hit')
        if tmp < 0:
            character.temp_hit = 0
        else:
            character.temp_hit = tmp
        character.save()
        return Response(status.HTTP_200_OK)


class HealPatch(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def patch(self, request, character_id):
        character = get_object_or_404(Character, pk=character_id)
        heal = request.data.get('heal')
        current_hit = character.current_hit
        current_hit += int(heal)
        if current_hit > character.max_hit:
            current_hit = character.max_hit
        character.current_hit = current_hit
        character.save()
        return Response({'current_hit': current_hit}, status.HTTP_200_OK)


class DamagePatch(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def patch(self, request, character_id):
        character = get_object_or_404(Character, pk=character_id)
        damage = request.data.get('damage')
        # Текущие значения здоровья
        current_hit = character.current_hit
        temp_hit = character.temp_hit

        # Логика вычитания урона
        if temp_hit > 0:
            # Если есть временное здоровье, вычитаем урон из него
            if damage >= temp_hit:
                # Если урон больше или равен временному здоровью, полностью расходуем его
                damage -= temp_hit
                temp_hit = 0
            else:
                # Если урон меньше временного здоровья, вычитаем только часть
                temp_hit -= damage
                damage = 0

        # Если остался урон после временного здоровья, вычитаем его из основного здоровья
        if damage > 0:
            current_hit -= damage
            current_hit = max(current_hit, 0)  # Здоровье не может быть меньше 0

        # Обновляем значения в базе данных
        character.temp_hit = temp_hit
        character.current_hit = current_hit
        character.save()

        return Response({'current_hit': character.current_hit, 'temp_hit': character.temp_hit}, status.HTTP_200_OK)


class ItemView(viewsets.ReadOnlyModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Item.objects.all()
    filter_backends = [filters.SearchFilter, filters.OrderingFilter,
                       DjangoFilterBackend]
    serializer_class = ItemListsSerializer

    def retrieve(self, request, pk=None):
        item = get_object_or_404(Item, pk=pk)
        serializer = ItemsSerializer(item)
        return Response(serializer.data)

    def get_queryset(self):
        query = Q()
        search_query = self.request.query_params.get('search', '')
        rarity_params = self.request.query_params.getlist('rarity[]')
        queryset = Item.objects.all()
        for rarity in rarity_params:
            query |= Q(rarity__id=rarity)

        if search_query:
            query &= Q(name__iregex=search_query)
        queryset = queryset.filter(query).distinct()
        return queryset


class InventoryItemView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, character_id, pk):
        character = get_object_or_404(Character, id=character_id)
        # item_id = request.data.get('item_id')  # Получаем ID предмета
        quantity = request.data.get('quantity', 1)  # Количество (по умолчанию 1)
        # Проверяем, существует ли предмет
        item = get_object_or_404(Item, id=pk)
        # Проверяем, есть ли предмет уже в инвентаре
        inventory_item, created = InventoryItem.objects.get_or_create(
            character=character,
            item=item,
            defaults={'quantity': quantity}  # Если создается новый объект
        )
        if not created:
            # Если предмет уже существует, увеличиваем количество
            inventory_item.quantity += quantity
            inventory_item.save()
        # Сериализуем данные и возвращаем ответ
        serializer = InventorySerializer(inventory_item)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, character_id, pk):
        character = get_object_or_404(Character, id=character_id)
        item = get_object_or_404(Item, id=pk)  # Используем pk из URL
        # Находим предмет в инвентаре
        inventory_item = get_object_or_404(InventoryItem, character=character, item=item)
        # Удаляем предмет
        inventory_item.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self, request, character_id):
        character = get_object_or_404(Character, id=character_id)
        for item in request.data:
            item_id = int(item.get('item').get("id"))
            quantity = int(item.get('quantity'))
            put_on = item.get('put_on')
            inventory_item = get_object_or_404(InventoryItem,
                                               character=character,
                                               item__id=item_id)
            inventory_item.quantity = quantity
            inventory_item.put_on = put_on
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


class RandomDiceView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        # Получаем количество кубов из запроса
        dice_data = request.data
        result = {}
        total_sum = 0

        # Список типов кубов
        dice_types = ['d4', 'd6', 'd8', 'd10', 'd12', 'd20']

        for dice_type in dice_types:
            # Количество кубов для текущего типа
            count = dice_data.get(dice_type, 0)

            if count > 0:
                # Генерируем случайные числа для кубов
                rolls = [random.randint(1, int(dice_type[1:])) for _ in range(count)]
                result[dice_type] = rolls
                total_sum += sum(rolls)

        # Добавляем общую сумму в результат
        result['total'] = total_sum

        return Response(result)
