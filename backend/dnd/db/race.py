from django.db import models


class FeatureRace(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название особенности")
    description = models.TextField(verbose_name="Описание особенности")

    class Meta:
        verbose_name = "Общие особенности расы"
        verbose_name_plural = "Общие особенности расы"

    def __str__(self):
        return self.name


class CustomFeatureRace(models.Model):
    character = models.ForeignKey(
        'Character', on_delete=models.CASCADE, related_name='custom_features'
    )
    feature = models.ForeignKey(
        FeatureRace, on_delete=models.CASCADE, related_name='custom_features'
    )
    custom_description = models.TextField(
        verbose_name="Пользовательское описание", blank=True, null=True
    )
    hide_original = models.BooleanField(
        verbose_name="Скрыть оригинальный текст", default=False
    )

    class Meta:
        verbose_name = "Пользовательская общая особенность расы"
        verbose_name_plural = "Пользовательские общие особенности рас"

    def __str__(self):
        return f"{self.character.name_champion} - {self.feature.name}"


class RaceBackground(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название особенности")
    description = models.TextField(verbose_name="Описание особенности")

    class Meta:
        verbose_name = "Историческая особенность расы"
        verbose_name_plural = "Исторические особенности рас"

    def __str__(self):
        return self.name


class CustomRaceBackground(models.Model):
    character = models.ForeignKey(
        'Character', on_delete=models.CASCADE,
        related_name='custom_history_race_backgrounds'
    )
    race_background = models.ForeignKey(
        RaceBackground, on_delete=models.CASCADE,
        related_name='custom_history_race_backgrounds',
    )
    custom_description = models.TextField(
        verbose_name="Пользовательское описание", blank=True, null=True
    )
    hide_original = models.BooleanField(
        verbose_name="Скрыть оригинальный текст", default=False
    )

    class Meta:
        verbose_name = "Пользовательская историческая особенность расы"
        verbose_name_plural = "Пользовательские исторические особенности рас"

    def __str__(self):
        return f"{self.character.name_champion} - {self.race_background.name}"


class Race(models.Model):
    name = models.CharField(max_length=50, unique=True,
                            verbose_name="Название расы")
    description = models.TextField(verbose_name="Описание")
    background = models.ManyToManyField(RaceBackground, verbose_name="История "
                                                                     "рассы",
                                        related_name='races_backgrounds', )
    features = models.ManyToManyField(
        FeatureRace,
        related_name="races_features",
        verbose_name="Особенности"
    )

    class Meta:
        verbose_name = "Раса"
        verbose_name_plural = "Расы"

    def __str__(self):
        return self.name

    def get_race(self, obj):
        if not obj.race:
            return None

        race_data = {
            "id": obj.race.id,
            "name": obj.race.name,
            "description": obj.race.description,
            "features": self.get_features_with_custom(obj,
                                                      obj.race.features.all()),
            "backgrounds": self.get_backgrounds_with_custom(obj,
                                                            obj.race.background.all())
        }

        if obj.sub_race:
            race_data["sub_race"] = self.get_sub_race(obj)

        return race_data

    def get_sub_race(self, obj):
        if not obj.sub_race:
            return None

        return {
            "id": obj.sub_race.id,
            "name": obj.sub_race.name,
            "description": obj.sub_race.description,
            "features": self.get_features_with_custom(obj,
                                                      obj.sub_race.features.all()),
            "backgrounds": self.get_backgrounds_with_custom(obj,
                                                            obj.sub_race.background.all()),
            "race": obj.sub_race.race.id if obj.sub_race.race else None
        }

    def get_features_with_custom(self, obj, features):
        """
        Возвращает список особенностей с учетом пользовательских данных.
        """
        custom_features = CustomFeatureRace.objects.filter(character=obj)
        custom_map = {custom.feature_id: custom for custom in custom_features}

        result = []
        for feature in features:
            custom_data = custom_map.get(feature.id)
            feature_data = {
                "id": feature.id,
                "name": feature.name,
                "description": feature.description,
            }
            if custom_data:
                feature_data["custom"] = {
                    "custom_description": custom_data.custom_description,
                    "hide_original": custom_data.hide_original,
                }
            result.append(feature_data)

        return result

    def get_backgrounds_with_custom(self, obj, backgrounds):
        """
        Возвращает список фонов с учетом пользовательских данных.
        """
        custom_backgrounds = CustomRaceBackground.objects.filter(character=obj)
        custom_map = {custom.race_background_id: custom for custom in
                      custom_backgrounds}

        result = []
        for background in backgrounds:
            custom_data = custom_map.get(background.id)
            background_data = {
                "id": background.id,
                "name": background.name,
                "description": background.description,
            }
            if custom_data:
                background_data["custom"] = {
                    "custom_description": custom_data.custom_description,
                    "hide_original": custom_data.hide_original,
                }
            result.append(background_data)

        return result


class SubRace(models.Model):
    race = models.ForeignKey(
        Race,
        on_delete=models.CASCADE,
        related_name="subraces",
        verbose_name="Основная раса"
    )
    name = models.CharField(max_length=100, verbose_name="Название подвида")
    description = models.TextField(verbose_name="Описание")
    background = models.ManyToManyField(RaceBackground,
                                        verbose_name="История подвида",
                                        related_name='sub_races_backgrounds')
    features = models.ManyToManyField(
        FeatureRace,
        related_name="sub_races_features_race",
        verbose_name="Особенности подвида"
    )

    class Meta:
        verbose_name = "Подвид"
        verbose_name_plural = "Подвиды"

    def __str__(self):
        return f"{self.name} ({self.race.name})"
