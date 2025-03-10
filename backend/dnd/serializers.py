from rest_framework import serializers

from .db.character import *
from .db.inventory import Properties, TypeItem, Rarity, SubType, Weapon, \
    Equipment, Armor, MagicItems
from .db.lineament import CustomLineament
from .db.race import RaceBackground, CustomRaceBackground, FeatureRace, \
    CustomFeatureRace
from .models import *


# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ['url', 'username', 'email', 'groups']
#
#
# class GroupSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Group
#         fields = ['url', 'name']


class RaceBackgroundSerializer(serializers.ModelSerializer):
    class Meta:
        model = RaceBackground
        fields = ['id', 'name', 'description']


class CustomRaceBackgroundSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomRaceBackground
        fields = ['id', 'custom_description', 'hide_original']


class FeatureRaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeatureRace
        fields = ['id', 'name', 'description']


class CustomFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomFeatureRace
        fields = ['id', 'custom_description', 'hide_original']


class CreateRaceSerializer(serializers.ModelSerializer):
    name = serializers.CharField()

    class Meta:
        model = Race
        fields = ['id', 'name']


class RaceSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    features = FeatureRaceSerializer(many=True, required=False)
    backgrounds = RaceBackgroundSerializer(source='background', many=True,
                                           required=False)

    class Meta:
        model = Race
        fields = ['id', 'name', 'description', 'features', 'backgrounds']


class SubRaceSerializer(serializers.ModelSerializer):
    features = FeatureRaceSerializer(many=True)
    backgrounds = RaceBackgroundSerializer(source='background', many=True)

    class Meta:
        model = SubRace
        fields = ['id', 'name', 'description', 'features', 'backgrounds',
                  'race']


class WorldOutlookSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorldOutlook
        fields = '__all__'


class BackgroundSerializer(serializers.ModelSerializer):
    class Meta:
        model = BackgroundModel
        fields = '__all__'


class ProtectStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProtectStateModel
        fields = '__all__'


class SkillStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SkillStateModel
        fields = '__all__'


class ChampionSpellSerializer(serializers.ModelSerializer):
    class Meta:
        model = Spell
        fields = '__all__'


class PropertiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Properties
        fields = '__all__'


class TypeItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeItem
        fields = '__all__'


class RaritySerializer(serializers.ModelSerializer):
    class Meta:
        model = Rarity
        fields = '__all__'


class WeaponTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubType
        fields = '__all__'


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'


class WeaponSerializer(serializers.ModelSerializer):
    item = ItemSerializer()

    class Meta:
        model = Weapon
        fields = '__all__'

    def to_representation(self, instance):
        data = super(WeaponSerializer, self).to_representation(instance)
        copy_data = data.copy()
        for i in data:
            if not data[i]:
                copy_data.pop(i)
        return copy_data


class EquipmentSerializer(serializers.ModelSerializer):
    item = ItemSerializer()

    class Meta:
        model = Equipment
        fields = '__all__'

    def to_representation(self, instance):
        data = super(EquipmentSerializer, self).to_representation(instance)
        copy_data = data.copy()
        for i in data:
            if not data[i]:
                copy_data.pop(i)
        return copy_data


class ArmorSerializer(serializers.ModelSerializer):
    item = ItemSerializer()

    class Meta:
        model = Armor
        fields = '__all__'

    def to_representation(self, instance):
        data = super(ArmorSerializer, self).to_representation(instance)
        copy_data = data.copy()
        for i in data:
            if not data[i]:
                copy_data.pop(i)
        return copy_data


class MagicItemsSerializer(serializers.ModelSerializer):
    item = ItemSerializer()

    class Meta:
        model = MagicItems
        fields = '__all__'

    def to_representation(self, instance):
        data = super(MagicItemsSerializer, self).to_representation(instance)
        copy_data = data.copy()
        for i in data:
            if not data[i]:
                copy_data.pop(i)
        return copy_data


class ItemsSerializer(serializers.ModelSerializer):
    rarity = RaritySerializer()
    weapon = WeaponSerializer(allow_null=True)
    armor = ArmorSerializer(allow_null=True)
    equipment = EquipmentSerializer(allow_null=True)
    magic_item = MagicItemsSerializer(allow_null=True)
    type = TypeItemSerializer()

    class Meta:
        model = Item
        fields = '__all__'

    def to_representation(self, instance):
        data = super(ItemsSerializer, self).to_representation(instance)
        if not data['armor']:
            del data['armor']
        if not data['weapon']:
            del data['weapon']
        if not data['equipment']:
            del data['equipment']
        if not data['magic_item']:
            del data['magic_item']
        return data


class SpellBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Spell
        fields = ['id', 'name', 'lvl', 'class_actor']


class OriginListSerializer(serializers.ModelSerializer):
    class Meta:
        model = OriginModel
        fields = ['id', 'name']


class Origin(serializers.ModelSerializer):
    class Meta:
        model = OriginModel
        fields = ['id', 'name', 'description']


class RaceBackgroundSerializer(serializers.ModelSerializer):
    class Meta:
        model = BackgroundModel


class SpellSerializer(serializers.ModelSerializer):
    class Meta:
        model = Spell
        fields = "__all__"


class InventorySerializer(serializers.ModelSerializer):
    item = ItemsSerializer()
    quantity = serializers.IntegerField()

    class Meta:
        model = InventoryItem
        fields = "__all__"


class CustomSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomLineament
        fields = "__all__"


class LineamentSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    description = serializers.CharField()
    custom = CustomSerializer(many=True, )

    class Meta:
        model = LineamentModel
        fields = "__all__"


class RaceListSerializer(serializers.ModelSerializer):
    """Сериализатор для списка расс."""

    class Meta:
        model = Race
        fields = ['id', 'name']


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


class ArchetypeSerializer(serializers.ModelSerializer):
    """Сериализатор для архетипов."""
    levels = serializers.SerializerMethodField()

    class Meta:
        model = Archetype
        fields = ['name', 'description', 'levels']

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


class CharacterSerializer(serializers.ModelSerializer):
    account = serializers.HiddenField(default=serializers.CurrentUserDefault())
    """Сериализатор для персонажа."""
    champion_class = BaseClassSerializer()
    archetype = ArchetypeSerializer()
    race = RaceSerializer()
    origin = serializers.StringRelatedField()
    world_outlook = WorldOutlookSerializer()
    skill_state = SkillStateSerializer()
    protect_state = ProtectStateSerializer()

    class Meta:
        model = Character
        fields = [
            'id', 'champion_class', 'archetype', 'race', 'sub_race', 'skill_state', 'possession_bonus', 'protect_state', 'inspiration',
            'protection_class', 'speed', 'account', 'name_champion', 'level', 'origin', 'world_outlook', 'strength', 'dexterity',
            'constitution',
            'intelligence', 'wisdom', 'charisma',
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

        # Получаем или создаем объекты BaseClass и Race
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
