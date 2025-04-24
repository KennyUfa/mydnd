import math
import random

from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from character.models import Character, ProtectStateModel, SkillStateModel
from character.serializers import ProtectStateSerializer, SkillStateSerializer


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


class ProtectStateView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProtectStateSerializer
    queryset = ProtectStateModel.objects.all()


class SkillStateView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = SkillStateSerializer
    queryset = SkillStateModel.objects.all()


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
