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


class DndSpellSerializer(serializers.ModelSerializer):
    class Meta:
        model = DndSpell
        fields = ['name']

    def to_representation(self, instance):
        return instance.name


class CharlistSerializer(serializers.ModelSerializer):
    champion_class = serializers.SlugRelatedField(slug_field='champion_class',
                                                  queryset=BaseClassCh.objects.all())
    race = serializers.SlugRelatedField(slug_field='race', queryset=
    Race.objects.all())
    account = serializers.HiddenField(default=serializers.CurrentUserDefault())

    pre_history = serializers.CharField()
    # race = serializers.CharField(source='race.race',default='Нет',read_only=True)
    world_outlook = serializers.CharField()
    # spells = DndSpellSerializer(many=True, read_only=True)

    class Meta:
        model = Character
        fields = '__all__'


class ChampionClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseClassCh
        fields = '__all__'


