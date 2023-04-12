from django.contrib.auth.models import User, Group
from .models import *
from rest_framework import serializers


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
class WeaponTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeaponType
        fields = ['description']

class PropertiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Properties
        fields = ['name','description']
class WeaponSerializer(serializers.ModelSerializer):
    type = WeaponTypeSerializer()
    properties = PropertiesSerializer(many=True)
    class Meta:
        model = Weapon
        fields = '__all__'
class ShieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shield
        fields = '__all__'


class DndSpellBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = DndSpell
        fields = ['id', 'name', 'lvl', 'class_actor']


class CharlistSerializer(serializers.ModelSerializer):
    champion_class = serializers.SlugRelatedField(slug_field='champion_class',
                                                  queryset=BaseClassCh.objects.all(),
                                                  required=False)
    race = serializers.SlugRelatedField(slug_field='race', queryset=
    Race.objects.all(), required=False)
    account = serializers.HiddenField(default=serializers.CurrentUserDefault())

    pre_history = serializers.SlugRelatedField(slug_field='pre_history_choices',
                                               queryset=
                                               PreHistoryModel.objects.all(),
                                               required=False)
    world_outlook = serializers.SlugRelatedField(
        slug_field='world_outlook',
        queryset=WorldOutlook.objects.all(), required=False)
    weapon = WeaponSerializer(required=False,many=True, read_only=True,)
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
