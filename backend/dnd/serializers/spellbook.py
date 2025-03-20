from rest_framework import serializers
from dnd.db.magic import Spell, SpellSlotLevel, CharacterSpellSlotLevel, CharacterSpellSlots


class SpellSerializer(serializers.ModelSerializer):
    class Meta:
        model = Spell
        fields = '__all__'

class SpellSlotLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpellSlotLevel
        fields = ['id', 'level', 'count', 'used']

class CharacterSpellSlotLevelSerializer(serializers.ModelSerializer):
    spell_slot_level = SpellSlotLevelSerializer()  # Вложенный сериализатор для уровня
    spells = SpellSerializer(many=True, read_only=True)  # Список выбранных заклинаний

    class Meta:
        model = CharacterSpellSlotLevel
        fields = ['id', 'character_spell_slots', 'spell_slot_level', 'spells']

class CharacterSpellSlotsSerializer(serializers.ModelSerializer):
    levels = CharacterSpellSlotLevelSerializer(many=True, read_only=True, source='characterspellslotlevel_set')

    class Meta:
        model = CharacterSpellSlots
        fields = ['id', 'levels']
