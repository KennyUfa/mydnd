from .background_serializers import BackgroundSerializer
from .class_serializers import *
from .race_serializers import *
from .spellbook import CharacterSpellSlotsSerializer
from ..db.inventory import Properties, TypeItem, Rarity, SubType, Weapon, \
    Equipment, Armor, MagicItems
from ..db.lineament import CustomLineament
from ..models import *


class WorldOutlookSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorldOutlook
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
        depth = 3

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
            'protection_class', 'speed', 'account', 'name_champion', 'level', 'world_outlook', 'skills', 'background','my_items', 'spell_slots',
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
