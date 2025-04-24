from rest_framework import serializers
from worldoutlook.models import WorldOutlook


class WorldOutlookSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorldOutlook
        fields = '__all__'
