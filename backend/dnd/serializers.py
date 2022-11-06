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


class DndSpellSerializer(serializers.ModelSerializer):
    class Meta:
        model = DndSpell
        fields = ['name']

    def to_representation(self, instance):
        return instance.name


class CharlistSerializer(serializers.ModelSerializer):
    champion_class = serializers.CharField(source='champion_class.class_name')
    account = serializers.CharField(source='account.username')
    pre_history = serializers.CharField(source='pre_history.history')
    race = serializers.CharField(source='race.race')
    world_outlook = serializers.CharField(source='world_outlook.world_outlook')
    spells = DndSpellSerializer(many=True, read_only=True)

    class Meta:
        model = Character
        fields = '__all__'
