from rest_framework import serializers

from lineaments.models import CustomLineament, LineamentModel


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

