from django.db import models


class Background(models.Model):
    """
    Основная модель для предыстории.
    """
    name = models.CharField(max_length=100, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")

    class Meta:
        verbose_name = "Предыстория"
        verbose_name_plural = "Предыстории"

    def __str__(self):
        return self.name


class SkillsProficiency(models.Model):
    background_id = models.ForeignKey(Background, on_delete=models.CASCADE,
                                      related_name="skill_proficiencies",)
    name = models.CharField(max_length=255)
    skills_proficiency = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Feature(models.Model):
    """
    Особенности предыстории.
    """
    background = models.ForeignKey(
        Background,
        on_delete=models.CASCADE,
        related_name="features",
        verbose_name="Предыстория"
    )
    name = models.CharField(max_length=100, verbose_name="Название особенности")
    description = models.TextField(verbose_name="Описание")
    has_choice = models.BooleanField(default=False, verbose_name="Есть выбор")

    class Meta:
        verbose_name = "Особенность предыстории"
        verbose_name_plural = "Особенности предыстории"

    def __str__(self):
        return f"{self.name} ({self.background.name})"


class FeatureOption(models.Model):
    """
    Варианты для особенностей с выбором.
    """
    feature = models.ForeignKey(
        Feature,
        on_delete=models.CASCADE,
        related_name="options",
        verbose_name="Особенность"
    )
    name = models.CharField(max_length=100, verbose_name="Название варианта")

    class Meta:
        verbose_name = "Вариант особенности"
        verbose_name_plural = "Варианты особенностей"

    def __str__(self):
        return f"{self.name} ({self.feature.name})"


class SelectedFeatureOption(models.Model):
    """
    Модель для хранения выбранного варианта особенности.
    """
    character = models.ForeignKey(
        'Character',
        on_delete=models.CASCADE,
        related_name="selected_feature_options",
        verbose_name="Персонаж"
    )
    feature = models.ForeignKey(
        Feature,
        on_delete=models.CASCADE,
        related_name="selected_options",
        verbose_name="Особенность"
    )
    option = models.ForeignKey(
        FeatureOption,
        on_delete=models.CASCADE,
        related_name="selected_by",
        verbose_name="Выбранный вариант"
    )

    class Meta:
        verbose_name = "Выбранный вариант особенности"
        verbose_name_plural = "Выбранные варианты особенностей"

    def __str__(self):
        return f"{self.character.name_champion} выбрал {self.option.name} для {self.feature.name}"


class Trait(models.Model):
    """
    Черта характера.
    """
    background = models.ForeignKey(
        Background,
        on_delete=models.CASCADE,
        related_name="traits",
        verbose_name="Предыстория"
    )
    name = models.CharField(max_length=100, verbose_name="Название черты")

    class Meta:
        verbose_name = "Черта характера"
        verbose_name_plural = "Черты характера"

    def __str__(self):
        return f"{self.name} ({self.background.name})"


class Ideal(models.Model):
    """
    Идеалы.
    """
    background = models.ForeignKey(
        Background,
        on_delete=models.CASCADE,
        related_name="ideals",
        verbose_name="Предыстория"
    )
    name = models.CharField(max_length=100, verbose_name="Название идеала")

    class Meta:
        verbose_name = "Идеал"
        verbose_name_plural = "Идеалы"

    def __str__(self):
        return f"{self.name} ({self.background.name})"


class Bond(models.Model):
    """
    Привязанности.
    """
    background = models.ForeignKey(
        Background,
        on_delete=models.CASCADE,
        related_name="bonds",
        verbose_name="Предыстория"
    )
    name = models.CharField(max_length=100, verbose_name="Название привязанности")

    class Meta:
        verbose_name = "Привязанность"
        verbose_name_plural = "Привязанности"

    def __str__(self):
        return f"{self.name} ({self.background.name})"


class Flaw(models.Model):
    """
    Слабости.
    """
    background = models.ForeignKey(
        Background,
        on_delete=models.CASCADE,
        related_name="flaws",
        verbose_name="Предыстория"
    )
    name = models.CharField(max_length=100, verbose_name="Название слабости")

    class Meta:
        verbose_name = "Слабость"
        verbose_name_plural = "Слабости"

    def __str__(self):
        return f"{self.name} ({self.background.name})"


class SelectedOrigin(models.Model):
    character = models.ForeignKey(
        'Character',
        on_delete=models.CASCADE,
        related_name="selected_origin_options",
        verbose_name="Выбор предыстории"
    )
    flaw = models.ForeignKey(Flaw, on_delete=models.CASCADE, related_name="selected_by",verbose_name="Выбранная слабость",blank=True,
                             null=True)
    bond = models.ForeignKey(Bond, on_delete=models.CASCADE, related_name="selected_by", verbose_name="Выбранная привязанность",blank=True,
                             null=True)
    trait = models.ForeignKey(Trait, on_delete=models.CASCADE, related_name="selected_by", verbose_name="Выбранная черта",blank=True,
                             null=True)
    ideal = models.ForeignKey(Ideal, on_delete=models.CASCADE, related_name="selected_by", verbose_name="Выбранный идеал",blank=True,
                             null=True)
