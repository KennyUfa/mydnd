from rest_framework import serializers

from spellbook.models import Spell, SpellSlotLevel, CharacterSpellSlotLevel, CharacterSpellSlots


class SpellSerializer(serializers.ModelSerializer):
    class_actor = serializers.StringRelatedField(many=True, read_only=True)
    archetypes = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = Spell
        fields = '__all__'


class SpellPreviewSerializer(serializers.ModelSerializer):
    class_actor = serializers.StringRelatedField(many=True,read_only=True)
    class Meta:
        model = Spell
        fields = ['id','class_actor', 'name', 'level', 'archetype', 'school']


class SpellSlotLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpellSlotLevel
        fields = ['id', 'level', 'count', 'used']


class CharacterSpellSlotLevelSerializer(serializers.ModelSerializer):
    spells = serializers.SerializerMethodField()
    spell_slot_level = SpellSlotLevelSerializer(read_only=True)

    def get_spells(self, obj):
        # Получаем список ID заклинаний из JSONField
        spell_ids = obj.spells
        # Создаем словарь что бы не дублировать запросы к базе данных
        spells_dict = {spell.id: SpellPreviewSerializer(spell).data for spell in Spell.objects.filter(id__in=spell_ids)}
        # Возвращаем данные о заклинаниях в том же порядке, что и в spell_ids
        return [spells_dict.get(spell_id) for spell_id in spell_ids]

    class Meta:
        model = CharacterSpellSlotLevel
        fields = ['id', 'spell_slot_level', 'spells']


class CharacterSpellSlotsSerializer(serializers.ModelSerializer):
    slot_levels = CharacterSpellSlotLevelSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = CharacterSpellSlots
        fields = ['id', 'slot_levels']
