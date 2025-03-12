from django.db import models


class SmallFeaturesRace(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название особенности")
    description = models.TextField(verbose_name="Описание особенности")

    class Meta:
        verbose_name = "Общие особенности расы"
        verbose_name_plural = "Общие особенности расы"

    def __str__(self):
        return self.name


class CustomSmallFeaturesRace(models.Model):
    character = models.ForeignKey(
        'Character', on_delete=models.CASCADE, related_name='custom_features'
    )
    feature = models.ForeignKey(
        SmallFeaturesRace, on_delete=models.CASCADE, related_name='custom_features'
    )
    custom_description = models.TextField(
        verbose_name="Пользовательское описание", blank=True, null=True
    )
    hide_original = models.BooleanField(default=False)
    hide_custom = models.BooleanField(default=True)

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
    hide_original = models.BooleanField(default=False)
    hide_custom = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Пользовательская историческая особенность расы"
        verbose_name_plural = "Пользовательские исторические особенности рас"

    def __str__(self):
        return f"{self.character.name_champion} - {self.race_background.name}"


class Race(models.Model):
    name = models.CharField(max_length=50,
                            verbose_name="Название расы")
    description = models.TextField(verbose_name="Описание", blank=True, null=True)
    background = models.ManyToManyField(RaceBackground, verbose_name="История "
                                                                     "рассы",
                                        related_name='race',
                                        blank=True)
    features = models.ManyToManyField(
        SmallFeaturesRace,
        related_name="race",
        verbose_name="Особенности", blank=True
    )

    class Meta:
        verbose_name = "Раса"
        verbose_name_plural = "Расы"

    def __str__(self):
        return self.name


class SubRace(models.Model):
    race = models.ForeignKey(
        Race,
        on_delete=models.CASCADE,
        related_name="sub_race",
        verbose_name="Основная раса"
    )
    name = models.CharField(max_length=100, verbose_name="Название подвида")
    description = models.TextField(verbose_name="Описание")
    background = models.ManyToManyField(RaceBackground,
                                        verbose_name="История подвида",
                                        related_name='sub_races_backgrounds')
    features = models.ManyToManyField(
        SmallFeaturesRace,
        related_name="sub_race",
        verbose_name="Особенности подвида"
    )

    class Meta:
        verbose_name = "Подвид"
        verbose_name_plural = "Подвиды"

    def __str__(self):
        return f"{self.name} ({self.race.name})"
