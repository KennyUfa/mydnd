from rest_framework import serializers

from dnd.db.background import Background, SkillsProficiency, Feature, FeatureOption, SelectedFeatureOption, Trait, Ideal, Bond, Flaw, \
    SelectedOrigin


class SkillsProficiencySerializer(serializers.ModelSerializer):
    background_id = serializers.PrimaryKeyRelatedField(queryset=Background.objects.all(), source='background_id.id')

    class Meta:
        model = SkillsProficiency
        fields = ['id', 'background_id', 'name', 'skills_proficiency']


class FeatureOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeatureOption
        fields = ['id', 'name']


class FeatureSerializer(serializers.ModelSerializer):
    options = FeatureOptionSerializer(many=True, read_only=True)
    selected_options = serializers.SerializerMethodField()

    def get_selected_options(self, obj):
        # Получаем все выбранные опции для данной особенности
        selected_options = SelectedFeatureOption.objects.filter(feature=obj)
        return SelectedFeatureOptionSerializer(selected_options, many=True).data

    class Meta:
        model = Feature
        fields = ['id', 'background', 'name', 'description', 'has_choice', 'options', 'selected_options']


class TraitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trait
        fields = ['id', 'background', 'name']


class IdealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ideal
        fields = ['id', 'background', 'name']


class BondSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bond
        fields = ['id', 'background', 'name']


class FlawSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flaw
        fields = ['id', 'background', 'name']


class SelectedFeatureOptionSerializer(serializers.ModelSerializer):
    feature_name = serializers.CharField(source='feature.name', read_only=True)
    option_name = serializers.CharField(source='option.name', read_only=True)

    class Meta:
        model = SelectedFeatureOption
        fields = ['id', 'character', 'feature', 'option', 'feature_name', 'option_name']


class SelectedOriginSerializer(serializers.ModelSerializer):
    flaw = FlawSerializer()
    bond = BondSerializer()
    trait = TraitSerializer()
    ideal = IdealSerializer()

    class Meta:
        model = SelectedOrigin
        fields = ['id', 'character', 'flaw', 'bond', 'trait', 'ideal']


class BackgroundListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Background
        fields = ['id', 'name', 'description']


class BackgroundSerializer(serializers.ModelSerializer):
    skill_proficiencies = SkillsProficiencySerializer(many=True, read_only=True)
    features = FeatureSerializer(many=True, read_only=True)
    selected_origins = serializers.SerializerMethodField()
    trait = TraitSerializer(many=True, read_only=True, source='traits')
    ideal = IdealSerializer(many=True, read_only=True, source='ideals')
    bond = BondSerializer(many=True, read_only=True, source='bonds')
    flaw = FlawSerializer(many=True, read_only=True, source='flaws')


    def get_selected_origins(self, obj):
        character = self.context.get('character')
        try:
            selected_origins = SelectedOrigin.objects.get(character=character)
        except SelectedOrigin.DoesNotExist:
            return []
        return SelectedOriginSerializer(selected_origins).data if selected_origins else []

    class Meta:
        model = Background
        fields = ['id', 'name', 'description', 'skill_proficiencies', 'features', 'trait',
                  'ideal', 'bond', 'flaw', 'selected_origins']
