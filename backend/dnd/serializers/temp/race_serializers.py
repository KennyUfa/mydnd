# from rest_framework import serializers
#
# from dnd.db.temp.race import CustomRaceBackground, RaceBackground, SmallFeaturesRace, CustomSmallFeaturesRace, Race, SubRace
#
#
# class RaceListSerializer(serializers.ModelSerializer):
#     """Сериализатор для списка рас."""
#
#     class Meta:
#         model = Race
#         fields = ['id', 'name']
#
#
# class RaceBackgroundSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = RaceBackground
#         fields = ['id', 'name', 'description']
#
#
# class CustomRaceBackgroundSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CustomRaceBackground
#         fields = ['id', 'custom_description', 'hide_original']
#
#
# class SmallFeatureSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = SmallFeaturesRace
#         fields = ['id', 'name', 'description']
#
#
# class CustomFeatureSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CustomSmallFeaturesRace
#         fields = ['id', 'custom_description', 'hide_original']
#
#
# class CreateRaceSerializer(serializers.ModelSerializer):
#     name = serializers.CharField()
#
#     class Meta:
#         model = Race
#         fields = ['id', 'name']
#
#
# class SubRaceSerializer(serializers.ModelSerializer):
#     features = SmallFeatureSerializer(many=True)
#     backgrounds = RaceBackgroundSerializer(source='background', many=True)
#
#     class Meta:
#         model = SubRace
#         fields = ['id', 'name', 'description', 'features', 'backgrounds',
#                   'race']
#
#
# class RaceSerializer(serializers.ModelSerializer):
#     name = serializers.CharField()
#     features = SmallFeatureSerializer(many=True, required=False)
#     backgrounds = RaceBackgroundSerializer(source='background', many=True,
#                                            required=False)
#     sub_race = serializers.SerializerMethodField()
#
#     def get_sub_race(self, obj):
#         try:
#             sub_race_id = self.context.get('character').sub_race.id
#         except AttributeError:
#             return  None
#         return SubRaceSerializer(SubRace.objects.get(id=sub_race_id)).data
#
#     class Meta:
#         model = Race
#         fields = ['id', 'name', 'description', 'features', 'backgrounds', 'sub_race']
