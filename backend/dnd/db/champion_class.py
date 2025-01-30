from django.db import models


class BaseClass(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название класса")
    description = models.TextField(verbose_name="Описание класса", blank=True,
                                   null=True)
    hit_dice = models.CharField(max_length=10, verbose_name="Кость хитов",
                                blank=True, null=True)
    hit_at_first_level = models.CharField(max_length=10, verbose_name="Хиты "
                                                                      "на "
                                                                      "первом уровне",
                                          blank=True, null=True)

    hit_at_next_level = models.CharField(max_length=100, verbose_name="Хиты "
                                                                      "на следующих уровнях",
                                         blank=True, null=True)
    possession_armor = models.CharField(max_length=100, verbose_name=
    "Владение доспехами", blank=True, null=True)
    possession_weapon = models.CharField(max_length=100, verbose_name=
    "Владение оружием", blank=True, null=True)
    possession_instrument = models.CharField(max_length=100,
                                             verbose_name="Владение инструментами",
                                             blank=True, null=True)
    saving_throws = models.CharField(max_length=100, verbose_name=
    "Спасброски", blank=True, null=True)

    class_skills = models.CharField(max_length=100, verbose_name=
    "Классовые навыки", blank=True, null=True)

    def __str__(self):
        return self.name

    def get_current_level_data(self, character_level, obj):
        levels = self.levels.filter(level__lte=character_level).order_by(
            'level')
        custom_abilities = CustomAbility.objects.filter(character=obj)
        custom_map = {custom.ability.id: custom for custom in custom_abilities}

        abilities = {}
        for level in levels:
            level_abilities = []

            for ability in level.abilities.all():
                custom_data = custom_map.get(ability.id)
                data = {"name": ability.name, "description":
                    ability.description,'id': ability.id}
                if custom_data:
                    data["custom"] = {
                        "description": custom_data.custom_description,
                        "hide_original": custom_data.hide_original,
                        'id': custom_data.id
                    }
                level_abilities.append(data)
            if level_abilities:
                abilities[str(level.level)] = level_abilities

        return {
            "level": character_level,
            "proficiency_bonus": levels.get(
                level=character_level).proficiency_bonus,
            "specific_columns": {
                column.name: column.values.get(level=character_level).value
                for column in self.specific_columns.all()
            },
            "abilities": abilities
        }


class Level(models.Model):
    class_obj = models.ForeignKey(BaseClass, on_delete=models.CASCADE,
                                  related_name="levels", verbose_name="Класс")
    level = models.PositiveIntegerField(verbose_name="Уровень")
    proficiency_bonus = models.PositiveIntegerField(
        verbose_name="Бонус мастерства")

    class Meta:
        unique_together = (
            "class_obj", "level")  # Уровень уникален в рамках класса
        ordering = ["class_obj", "level"]

    def __str__(self):
        return f"{self.class_obj.name} - Уровень {self.level}"


class Ability(models.Model):
    level = models.ForeignKey(Level, on_delete=models.CASCADE,
                              related_name="abilities", verbose_name="Уровень")
    name = models.CharField(max_length=255, verbose_name="Название способности")
    description = models.TextField(verbose_name="Описание способности",
                                   max_length=5000, blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.level.class_obj.name} - Уровень {self.level.level})"


class SpecificColumn(models.Model):
    class_obj = models.ForeignKey(BaseClass, on_delete=models.CASCADE,
                                  related_name="specific_columns",
                                  verbose_name="Класс")
    name = models.CharField(max_length=255,
                            verbose_name="Название специфического столбца")

    def __str__(self):
        return f"{self.name} ({self.class_obj.name})"


class CustomAbility(models.Model):
    character = models.ForeignKey('Character', on_delete=models.CASCADE,
                                  related_name='custom_attributes_class_character')
    ability = models.ForeignKey(Ability, on_delete=models.CASCADE,
                                related_name='custom_attributes_class_ability')
    custom_description = models.TextField(blank=True, null=True, )
    hide_original = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Пользовательская особенность класса"
        verbose_name_plural = "Пользовательские особенности класса"

    def __str__(self):
        return f"{self.character.name_champion} - {self.ability.name}"


class SpecificColumnValue(models.Model):
    specific_column = models.ForeignKey(SpecificColumn,
                                        on_delete=models.CASCADE,
                                        related_name="values",
                                        verbose_name="Специфический столбец")
    level = models.ForeignKey(Level, on_delete=models.CASCADE,
                              related_name="specific_column_values",
                              verbose_name="Уровень")
    value = models.JSONField(
        verbose_name="Значение")  # Хранение сложных данных (списков, словарей)

    class Meta:
        unique_together = (
            "specific_column",
            "level")  # Значение уникально для столбца и уровня

    def __str__(self):
        return f"{self.specific_column.name} ({self.level.class_obj.name} - Уровень {self.level.level}): {self.value}"


class Archetype(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название архетипа")
    character_class = models.ForeignKey(
        BaseClass, on_delete=models.CASCADE, related_name="archetypes",
        verbose_name="Класс"
    )
    description = models.TextField(
        verbose_name="Описание архетипа", blank=True, null=True
    )

    def get_current_level_data(self, character_level):
        levels = self.levels.filter(level__lte=character_level).order_by(
            'level')

        abilities = {}
        for level in levels:
            level_abilities = [ability.name for ability in
                               level.abilities.all()]
            if level_abilities:
                abilities[str(level.level)] = level_abilities

        specific_columns = {
            column.name: column.values.get(level=character_level).value
            for column in self.specific_columns.all()
        }

        return {
            "archetype_abilities": abilities,
            "archetype_specific_columns": specific_columns,
        }

    def __str__(self):
        return f"{self.name} ({self.character_class.name})"


class ArchetypeLevel(models.Model):
    archetype = models.ForeignKey(
        Archetype, on_delete=models.CASCADE, related_name="levels",
        verbose_name="Архетип"
    )
    level = models.PositiveIntegerField(verbose_name="Уровень")

    class Meta:
        unique_together = ("archetype", "level")
        ordering = ["archetype", "level"]

    def __str__(self):
        return f"{self.archetype.name} - Уровень {self.level}"


class ArchetypeAbility(models.Model):
    level = models.ForeignKey(
        ArchetypeLevel, on_delete=models.CASCADE, related_name="abilities",
        verbose_name="Уровень"
    )
    name = models.CharField(max_length=255, verbose_name="Название способности")
    description = models.TextField(
        verbose_name="Описание способности", max_length=500, blank=True,
        null=True
    )

    def __str__(self):
        return f"{self.name} ({self.level.archetype.name} - Уровень {self.level.level})"


class ArchetypeSpecificColumn(models.Model):
    archetype = models.ForeignKey(
        Archetype, on_delete=models.CASCADE, related_name="specific_columns",
        verbose_name="Архетип"
    )
    name = models.CharField(
        max_length=255, verbose_name="Название специфического столбца"
    )

    def __str__(self):
        return f"{self.name} ({self.archetype.name})"


class ArchetypeSpecificColumnValue(models.Model):
    specific_column = models.ForeignKey(
        ArchetypeSpecificColumn, on_delete=models.CASCADE,
        related_name="values",
        verbose_name="Специфический столбец"
    )
    level = models.ForeignKey(
        ArchetypeLevel, on_delete=models.CASCADE,
        related_name="specific_column_values", verbose_name="Уровень"
    )
    value = models.JSONField(verbose_name="Значение")

    class Meta:
        unique_together = ("specific_column", "level")

    def __str__(self):
        return (
            f"{self.specific_column.name} ({self.level.archetype.name} - "
            f"Уровень {self.level.level}): {self.value}"
        )
