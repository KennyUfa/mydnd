from django.contrib.auth.models import User, Group
from rest_framework import serializers

from .models import *


class SecondaryModel1Serializer(serializers.ModelSerializer):
    class Meta:
        model = SecondaryModel1
        fields = ['additional_info']  # Замените на поля SecondaryModel1


class SecondaryModel2Serializer(serializers.ModelSerializer):
    class Meta:
        model = SecondaryModel2
        fields = ['additional_info', 'info']  # Замените на поля SecondaryModel2


class SecondaryModel3Serializer(serializers.ModelSerializer):
    class Meta:
        model = SecondaryModel3
        fields = ['additional_info']  # Замените на поля SecondaryModel3


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class BaseClassChSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassChampion
        fields = "__all__"


# class RaceSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Race
#         fields = ['race']
class RaceSerializer(serializers.ModelSerializer):
    secondary_model1 = serializers.SerializerMethodField()
    secondary_model2 = serializers.SerializerMethodField()
    secondary_model3 = serializers.SerializerMethodField()

    class Meta:
        model = Race
        fields = ['race', 'secondary_model1', 'secondary_model2', 'secondary_model3']

    def get_secondary_model1(self, obj):
        if obj.secondarymodel1_set.exists():
            return SecondaryModel1Serializer(obj.secondarymodel1_set.all(), many=True).data
        return None

    def get_secondary_model2(self, obj):
        if obj.secondarymodel2_set.exists():
            return SecondaryModel2Serializer(obj.secondarymodel2_set.all(), many=True).data
        return None

    def get_secondary_model3(self, obj):
        if obj.secondarymodel3_set.exists():
            return SecondaryModel3Serializer(obj.secondarymodel3_set.all(), many=True).data
        return None

    def to_representation(self, instance):
        # Удалить пустые модели из вывода
        representation = super().to_representation(instance)
        return {
            key: value for key, value in representation.items() if value is not None
        }


class IdealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ideal
        fields = '__all__'


class OriginChoiceSerializer(serializers.ModelSerializer):
    origin = serializers.CharField()
    ideals = IdealSerializer(many=True)
    # ideal_choice = IdealSerializer()

    class Meta:
        model = Origin
        fields = '__all__'


class OriginSerializer(serializers.ModelSerializer):
    origin = serializers.CharField()

    class Meta:
        model = Origin
        fields = ['origin']


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


class SpellSerializer(serializers.ModelSerializer):
    class Meta:
        model = Spell
        fields = "__all__"


class ChampionClassSerializer(serializers.ModelSerializer):
    class_spells = SpellSerializer(many=True, read_only=True)

    class Meta:
        model = ClassChampion
        fields = "__all__"


class InventorySerializer(serializers.ModelSerializer):
    item = ItemsSerializer()
    quantity = serializers.IntegerField()

    class Meta:
        model = InventoryItem
        fields = "__all__"


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['name', 'level', 'description']


class CharacterSerializerList:
    class Meta:
        model = Character
        fields = ["name_champion", "champion_class", "lvl"]


class SpellLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpellLevel
        fields = ['level', 'spell_slots', 'known_conspiracies', 'known_spell']


class CharacterSerializer(serializers.ModelSerializer):
    champion_class = ChampionClassSerializer()
    race = serializers.SlugRelatedField(slug_field='race',
                                        queryset=Race.objects.all(),
                                        required=False)
    account = serializers.HiddenField(default=serializers.CurrentUserDefault())

    my_origin = OriginSerializer()
    world_outlook = serializers.SlugRelatedField(
        slug_field='name',
        queryset=WorldOutlook.objects.all(), required=False)
    background = BackgroundSerializer(required=False)
    protect_char_state = ProtectStateSerializer(required=False)
    skill_char_state = SkillStateSerializer(required=False)
    spells = ChampionSpellSerializer(many=True, read_only=True, required=False)
    spells_id = serializers.PrimaryKeyRelatedField(many=True,
                                                   queryset=Spell.objects.all(),
                                                   source='spells',
                                                   required=False)
    my_items = InventorySerializer(many=True, read_only=True)
    available_skills = serializers.SerializerMethodField()
    # ideal_choice = IdealSerializer()

    def get_available_skills(self, obj):
        return SkillSerializer(obj.champion_class.get_available_skills(obj.lvl), many=True).data

    # def get_spell_slots(self, obj):
    #     return SpellLevelSerializer(obj.champion_class.get_spell_slots(obj.lvl)).data

    class Meta:
        model = Character
        fields = '__all__'

    def create(self, validated_data):
        champion_class_data = validated_data.pop('champion_class')
        champion_class = ClassChampion.objects.get(champion_class=champion_class_data['champion_class'])
        character = Character.objects.create(champion_class=champion_class, **validated_data)
        return character

    # https://riptutorial.com/django-rest-framework/example/25521/updatable-nested-serializers
    def update(self, instance, validated_data):
        print(self.context['request'].data)

        if 'background' in validated_data:
            nested_serializer = self.fields['background']
            nested_instance = instance.background
            nested_data = validated_data.pop('background')
            nested_serializer.update(nested_instance, nested_data)
            print(nested_instance)
            print(nested_data)

        if 'protect_char_state' in validated_data:
            nested_serializer = self.fields['protect_char_state']
            nested_instance = instance.protect_char_state
            nested_data = validated_data.pop('protect_char_state')
            nested_serializer.update(nested_instance, nested_data)

        if 'skill_char_state' in validated_data:
            nested_serializer = self.fields['skill_char_state']
            nested_instance = instance.skill_char_state
            nested_data = validated_data.pop('skill_char_state')
            nested_serializer.update(nested_instance, nested_data)

        return super(CharacterSerializer, self).update(instance,
                                                       validated_data)
