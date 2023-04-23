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
        model = BaseClassCh
        fields = ['champion_class']


class RaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Race
        fields = ['race']


class PreHistorySerializer(serializers.ModelSerializer):
    pre_history_choices = serializers.CharField()

    class Meta:
        model = PreHistoryModel
        fields = '__all__'


class ChampionClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseClassCh
        fields = '__all__'


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
        model = DndSpell
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


class ItemSerializer:
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


class SuperItemSerializer(serializers.ModelSerializer):
    rarity = RaritySerializer()
    weapon = WeaponSerializer(allow_null=True)
    armor = ArmorSerializer(allow_null=True)
    type = TypeItemSerializer()

    class Meta:
        model = Item
        fields = '__all__'

    def to_representation(self, instance):
        data = super(SuperItemSerializer, self).to_representation(instance)
        if not data['armor']:
            del data['armor']
        if not data['weapon']:
            del data['weapon']
        return data


class DndSpellBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = DndSpell
        fields = ['id', 'name', 'lvl', 'class_actor']


class CharlistSerializer(serializers.ModelSerializer):
    champion_class = serializers.SlugRelatedField(slug_field='champion_class',
                                                  queryset=BaseClassCh.objects.all(),
                                                  required=False)
    race = serializers.SlugRelatedField(slug_field='race',
                                        queryset=Race.objects.all(),
                                        required=False)
    account = serializers.HiddenField(default=serializers.CurrentUserDefault())

    pre_history = serializers.SlugRelatedField(slug_field='pre_history_choices',
                                               queryset=
                                               PreHistoryModel.objects.all(),
                                               required=False)
    world_outlook = serializers.SlugRelatedField(
        slug_field='world_outlook',
        queryset=WorldOutlook.objects.all(), required=False)
    background = BackgroundSerializer(required=False)
    protect_char_state = ProtectStateSerializer(required=False)
    skill_char_state = SkillStateSerializer(required=False)
    spells = ChampionSpellSerializer(many=True, read_only=True, required=False)
    spells_id = serializers.PrimaryKeyRelatedField(many=True,
                                                   queryset=DndSpell.objects.all(),
                                                   source='spells',
                                                   required=False)

    class Meta:
        model = Character
        fields = '__all__'

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

        return super(CharlistSerializer, self).update(instance,
                                                      validated_data)
