from django.contrib.auth.models import User, Group
from rest_framework import serializers

from .models import *


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
        model = BaseClass
        fields = "__all__"

    def to_representation(self, instance):
        # Удалить пустые модели из вывода
        representation = super().to_representation(instance)
        return {
            key: value for key, value in representation.items() if
            value is not None
        }


class IdealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ideal
        fields = '__all__'


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
        model = CustomFeature
        fields = ['id', 'custom_description', 'hide_original']


class RaceSerializer(serializers.ModelSerializer):
    features = FeatureRaceSerializer(many=True)
    backgrounds = RaceBackgroundSerializer(source='background', many=True)

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


class CharacterSerializerList(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = ["champion_class", "name_champion", "lvl", "id"]


class BaseClassSerializer(serializers.ModelSerializer):
    table = serializers.SerializerMethodField()

    class Meta:
        model = BaseClass
        fields = ['name', 'description', 'table', 'hit_dice']

    def get_table(self, obj):
        # Получаем все уровни для класса
        levels = obj.levels.all().order_by('level')

        # Инициализируем структуру для таблицы
        table = {
            "columns": {
                "level": {},
                "proficiency_bonus": {},
                "abilities": {},
                "specific_columns": {}
            }
        }

        # Заполняем level, proficiency_bonus и abilities
        for level in levels:
            level_key = str(level.level)
            table["columns"]["level"][level_key] = level.level
            table["columns"]["proficiency_bonus"][
                level_key] = level.proficiency_bonus
            table["columns"]["abilities"][level_key] = [ability.name for ability
                                                        in
                                                        level.abilities.all()]

        # Заполняем specific_columns
        specific_columns = obj.specific_columns.all()
        for column in specific_columns:
            column_name = column.name
            table["columns"]["specific_columns"][column_name] = {
                str(value.level.level): value.value
                for value in column.values.all()
            }

        return table


class CharacterSerializer(serializers.ModelSerializer):
    champion_class = BaseClassSerializer()
    account = serializers.HiddenField(default=serializers.CurrentUserDefault())
    world_outlook = serializers.SlugRelatedField(
        slug_field='name',
        queryset=WorldOutlook.objects.all(), required=False)
    # background = BackgroundSerializer()
    protect_char_state = ProtectStateSerializer(required=False)
    skill_char_state = SkillStateSerializer(required=False)
    # spells = ChampionSpellSerializer(many=True, read_only=True, required=False)
    # spells_id = serializers.PrimaryKeyRelatedField(many=True,
    #                                                queryset=Spell.objects.all(),
    #                                                source='spells',
    #                                                required=False)
    # my_items = InventorySerializer(many=True, read_only=True)
    current_level_data = serializers.SerializerMethodField()
    race = RaceSerializer()
    sub_race = SubRaceSerializer(required=False)
    race_features = serializers.SerializerMethodField()
    race_backgrounds = serializers.SerializerMethodField()

    class Meta:
        model = Character
        fields = '__all__'

    # todo разделить бэйс класс и архетип
    def get_current_level_data(self, obj):
        current_level = obj.get_current_level_data()
        return current_level

    def get_race_features(self, obj):
        features = obj.race.features.all()
        custom_features = CustomFeature.objects.filter(character=obj)

        # Сопоставляем пользовательские данные с особенностями
        custom_features_map = {
            custom.feature_id: custom
            for custom in custom_features
        }

        # Добавляем кастомные данные к каждой особенности
        result = []
        for feature in features:
            custom_data = custom_features_map.get(feature.id)
            result.append({
                "id": feature.id,
                "name": feature.name,
                "description": feature.description,
                "custom": {
                    "custom_description": custom_data.custom_description if custom_data else None,
                    "hide_original": custom_data.hide_original if custom_data else False
                }
            })
        return result

    def get_race_backgrounds(self, obj):
        backgrounds = obj.race.background.all()
        custom_backgrounds = CustomRaceBackground.objects.filter(character=obj)

        # Сопоставляем пользовательские данные с историческими особенностями
        custom_backgrounds_map = {
            custom.race_background_id: custom
            for custom in custom_backgrounds
        }

        # Добавляем пользовательские данные к каждой исторической особенности
        result = []
        for background in backgrounds:
            custom_data = custom_backgrounds_map.get(background.id)
            result.append({
                "id": background.id,
                "name": background.name,
                "description": background.description,
                "custom": {
                    "custom_description": custom_data.custom_description if custom_data else None,
                    "hide_original": custom_data.hide_original if custom_data else False
                }
            })
        return result

    def create(self, validated_data):
        champion_class_data = validated_data.pop('champion_class')
        champion_class = BaseClass.objects.get(
            name=champion_class_data['champion_class'])
        character = Character.objects.create(champion_class=champion_class,
                                             **validated_data)
        return character

    # https://riptutorial.com/django-rest-framework/example/25521/updatable-nested-serializers
    def update(self, instance, validated_data):
        print(self.context['request'].data)

        for field in ['background', 'protect_char_state', 'skill_char_state']:
            if field in validated_data:
                nested_serializer = self.fields[field]
                nested_instance = getattr(instance, field)
                nested_data = validated_data.pop(field)
                nested_serializer.update(nested_instance, nested_data)
                print(nested_instance)
                print(nested_data)

        return super(CharacterSerializer, self).update(instance,
                                                       validated_data)
