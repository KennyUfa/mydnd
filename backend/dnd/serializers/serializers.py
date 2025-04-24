from rest_framework import serializers

from background.serializers import BackgroundSerializer
from champion_class.serializers import BaseClassSerializer, ArchetypeSerializer, BaseClassListSerializer
from item.serializers import InventorySerializer
from race.serializers import RaceListSerializer, RaceSerializer
from spellbook.serializers import CharacterSpellSlotsSerializer
from worldoutlook.serializers import WorldOutlookSerializer
from ..models import *


class ProtectStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProtectStateModel
        fields = '__all__'


class SkillStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SkillStateModel
        fields = '__all__'



class SkillsSerializer(serializers.ModelSerializer):
    """Сериализатор для навыков."""

    class Meta:
        model = Skills
        fields = "__all__"


class CreateCharacterSerializer(serializers.ModelSerializer):
    champion_class = BaseClassListSerializer()
    race = RaceListSerializer()

    class Meta:
        model = Character
        fields = [
            'id', 'champion_class', 'race', 'name_champion', 'level'
        ]

    def create(self, validated_data):
        # Извлекаем данные для champion_class и race
        champion_class_data = validated_data.pop('champion_class')
        race_data = validated_data.pop('race')

        # Получаем или создаем объекты BaseClass и RaceAndOrigin
        champion_class = BaseClass.objects.get(name=champion_class_data['name'])
        race = Race.objects.get(name=race_data['name'])

        # Создаем объект Character
        character = Character.objects.create(
            champion_class=champion_class,
            race=race,
            **validated_data
        )
        return character

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['champion_class'] = instance.champion_class.name if instance.champion_class else None
        representation['race'] = instance.race.name if instance.race else None
        return representation


class CharacterSerializerList(serializers.ModelSerializer):
    """Сериализатор для списка персонажей."""
    champion_class = serializers.StringRelatedField()
    race = serializers.StringRelatedField()

    class Meta:
        model = Character
        fields = ["champion_class", "name_champion", "level", "id", "race"]


class CharacterSerializer(serializers.ModelSerializer):
    account = serializers.HiddenField(default=serializers.CurrentUserDefault())
    """Сериализатор для персонажа."""
    champion_class = BaseClassSerializer()
    archetype = ArchetypeSerializer()
    race = RaceSerializer()
    background = BackgroundSerializer()
    world_outlook = WorldOutlookSerializer()
    skill_state = SkillStateSerializer()
    protect_state = ProtectStateSerializer()
    skills = SkillsSerializer()
    my_items = InventorySerializer(many=True)
    spell_slots = CharacterSpellSlotsSerializer(read_only=True)

    class Meta:
        model = Character
        fields = [
            'id', 'champion_class', 'archetype', 'race', 'sub_race', 'skill_state', 'possession_bonus', 'protect_state', 'inspiration',
            'protection_class', 'speed', 'account', 'name_champion', 'level', 'world_outlook', 'skills', 'background', 'my_items',
            'spell_slots', 'max_hit', 'current_hit', 'temp_hit'
        ]

    #     https://riptutorial.com/django-rest-framework/example/25521/updatable-nested-serializers
    def update(self, instance, validated_data):
        if 'skill_state' in validated_data:
            nested_serializer = self.fields['skill_state']
            nested_instance = instance.skill_state
            nested_data = validated_data.pop('skill_state')
            nested_serializer.update(nested_instance, nested_data)

        return super(CharacterSerializer, self).update(instance,
                                                       validated_data)
