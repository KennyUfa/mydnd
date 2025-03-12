from rest_framework import serializers

from dnd.db.character import *


class BaseClassListSerializer(serializers.ModelSerializer):
    """Сериализатор для списка базовых классов."""

    class Meta:
        model = BaseClass
        fields = ['id', 'name']


class SpellSlotSerializer(serializers.ModelSerializer):
    """Сериализатор для ячеек заклинаний."""

    class Meta:
        model = SpellSlot
        fields = ['slots']


class SpecificColumnSerializer(serializers.ModelSerializer):
    """Сериализатор для специфических колонок."""

    class Meta:
        model = SpecificColumn
        fields = ['name', 'value']


class CustomAbilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomAbility
        fields = [
            'id',
            'custom_description',
            'hide_original',
            'hide_custom']


class CustomAbilityPatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomAbility
        fields = [
            'id',
            'ability',
            'custom_description',
            'hide_original',
            'hide_custom'
        ]


class AbilitySerializer(serializers.ModelSerializer):
    """Сериализатор для способностей."""
    custom_description = serializers.SerializerMethodField()

    class Meta:
        model = Ability
        fields = ['name', 'description', 'custom_description', 'id', 'level_id']

    def get_custom_description(self, obj):
        # Получаем пользовательское описание для текущего персонажа
        character = self.context.get('character')
        if character:
            custom_ability = CustomAbility.objects.filter(
                character=character, ability=obj
            ).first()

            return {
                'id': custom_ability.id if custom_ability else None,
                'custom_description': custom_ability.custom_description if custom_ability else None,
                'hide_original': custom_ability.hide_original if custom_ability else False,
                'hide_custom': custom_ability.hide_custom if custom_ability else True,
            }
        return None


class LevelSerializer(serializers.ModelSerializer):
    """Сериализатор для уровней."""
    abilities = serializers.SerializerMethodField()
    specific_columns = serializers.SerializerMethodField()
    spell_slots = serializers.SerializerMethodField()

    class Meta:
        model = Level
        fields = ['level', 'proficiency_bonus', 'abilities', 'specific_columns',
                  'spell_slots']

    def get_abilities(self, obj):
        # Фильтруем способности по уровню персонажа
        character = self.context.get('character')
        if character and obj.level > character.level:
            return []
        abilities = obj.abilities.all()
        return AbilitySerializer(abilities, many=True,
                                 context=self.context).data

    def get_specific_columns(self, obj):
        # Возвращаем специфические колонки для уровня
        columns = obj.specific_column.all()
        return SpecificColumnSerializer(columns, many=True).data

    def get_spell_slots(self, obj):
        # Возвращаем ячейки заклинаний для уровня
        spell_slots = obj.spell_slots.first()
        return SpellSlotSerializer(spell_slots).data if spell_slots else None


class ArchetypeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Archetype
        fields = ['id', 'name']


class ArchetypeSerializer(serializers.ModelSerializer):
    """Сериализатор для архетипов."""
    levels = serializers.SerializerMethodField()

    class Meta:
        model = Archetype
        fields = ['id', 'name', 'description', 'levels']

    def get_levels(self, obj):
        # Фильтруем уровни по архетипу
        character = self.context.get('character')
        levels = obj.levels.all()
        if character:
            levels = levels.filter(level__lte=character.level)
        return LevelSerializer(levels, many=True, context=self.context).data


class BaseClassSerializer(serializers.ModelSerializer):
    """Сериализатор для базового класса."""
    archetypes = serializers.SerializerMethodField()
    levels = serializers.SerializerMethodField()

    class Meta:
        model = BaseClass
        fields = [
            'id',
            'name', 'description', 'hit_dice', 'hit_at_first_level',
            'hit_at_next_level', 'possession_armor', 'possession_weapon',
            'possession_instrument', 'saving_throws', 'class_skills',
            'archetypes', 'levels'
        ]

    def get_archetypes(self, obj):
        # Возвращаем архетипы для класса
        archetypes = obj.archetypes.all()
        return ArchetypeSerializer(archetypes, many=True,
                                   context=self.context).data

    def get_levels(self, obj):
        # Возвращаем уровни для класса
        character = self.context.get('character')
        levels = obj.levels.filter(archetype__isnull=True)
        if character:
            levels = levels.filter(level__lte=character.level)
        return LevelSerializer(levels, many=True, context=self.context).data
