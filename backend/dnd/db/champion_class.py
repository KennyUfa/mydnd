from django.db import models


class BaseClass(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название класса")
    description = models.TextField(verbose_name="Описание класса", blank=True,
                                   null=True)
    hit_dice = models.CharField(max_length=10, verbose_name="Кость хитов",
                                blank=True, null=True)
    hit_at_first_level = models.CharField(max_length=10,
                                          verbose_name="Хиты на первом уровне",
                                          blank=True, null=True)
    hit_at_next_level = models.CharField(max_length=100,
                                         verbose_name="Хиты на следующих уровнях",
                                         blank=True, null=True)
    possession_armor = models.CharField(max_length=100,
                                        verbose_name="Владение доспехами",
                                        blank=True, null=True)
    possession_weapon = models.CharField(max_length=100,
                                         verbose_name="Владение оружием",
                                         blank=True, null=True)
    possession_instrument = models.CharField(max_length=100,
                                             verbose_name="Владение инструментами",
                                             blank=True, null=True)
    saving_throws = models.CharField(max_length=100, verbose_name="Спасброски",
                                     blank=True, null=True)
    class_skills = models.CharField(max_length=100,
                                    verbose_name="Классовые навыки", blank=True,
                                    null=True)

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
                data = {
                    "name": ability.name,
                    "description": ability.description,
                    "custom": None
                }
                if ability.id in custom_map:
                    data["custom"] = {
                        "description": custom_map[
                            ability.id].custom_description,
                        "hide_original": custom_map[ability.id].hide_original
                    }
                level_abilities.append(data)
            if level_abilities:
                abilities[str(level.level)] = level_abilities

        specific_columns = {}
        for column in self.specific_columns.all():
            try:
                value = column.values.get(level__level=character_level).value
                specific_columns[column.name] = value
            except SpecificColumnValue.DoesNotExist:
                pass

        return {
            "level": character_level,
            "proficiency_bonus": levels.get(
                level=character_level).proficiency_bonus,
            "specific_columns": specific_columns,
            "abilities": abilities
        }


class Level(models.Model):
    class_obj = models.ForeignKey(BaseClass, on_delete=models.CASCADE,
                                  related_name="levels")
    level = models.PositiveIntegerField()
    proficiency_bonus = models.PositiveIntegerField()


class Ability(models.Model):
    level = models.ForeignKey(Level, on_delete=models.CASCADE,
                              related_name="abilities")
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)


class SpecificColumn(models.Model):
    class_obj = models.ForeignKey(BaseClass, on_delete=models.CASCADE,
                                  related_name="specific_columns")
    name = models.CharField(max_length=255)


class SpecificColumnValue(models.Model):
    specific_column = models.ForeignKey(SpecificColumn,
                                        on_delete=models.CASCADE,
                                        related_name="values")
    level = models.ForeignKey(Level, on_delete=models.CASCADE,
                              related_name="specific_column_values")
    value = models.JSONField()


class CustomAbility(models.Model):
    character = models.ForeignKey('Character', on_delete=models.CASCADE,
                                  related_name='custom_abilities')
    ability = models.ForeignKey(Ability, on_delete=models.CASCADE,
                                related_name='custom_versions')
    custom_description = models.TextField(blank=True, null=True)
    hide_original = models.BooleanField(default=False)


class Archetype(models.Model):
    name = models.CharField(max_length=100)
    character_class = models.ForeignKey(BaseClass, on_delete=models.CASCADE,
                                        related_name="archetypes")
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    def get_current_level_data(self, character_level, obj):
        levels = self.archetype_levels.filter(
            level__lte=character_level).order_by(
            'level')
        custom_abilities = ArchetypeCustomAbility.objects.filter(character=obj)
        custom_map = {custom.ability.id: custom for custom in custom_abilities}
        abilities = {}

        for level in levels:
            level_abilities = []
            for ability in level.archetype_abilities.all():
                data = {
                    "name": ability.name,
                    "description": ability.description,
                    "custom": None
                }
                if ability.id in custom_map:
                    data["custom"] = {
                        "description": custom_map[
                            ability.id].custom_description,
                        "hide_original": custom_map[ability.id].hide_original
                    }
                level_abilities.append(data)
            if level_abilities:
                abilities[str(level.level)] = level_abilities

        specific_columns = {}
        for column in self.archetype_specific_columns.all():
            try:
                value = column.values.get(level__level=character_level).value
                specific_columns[column.name] = value
            except ArchetypeSpecificColumnValue.DoesNotExist:
                pass

        return {
            "archetype_abilities": abilities,
            "archetype_specific_columns": specific_columns,
        }


class ArchetypeLevel(models.Model):
    archetype = models.ForeignKey(Archetype, on_delete=models.CASCADE,
                                  related_name="archetype_levels")
    level = models.PositiveIntegerField()

    def __str__(self):
        return str(f"{self.archetype.name} - {self.level}")


class ArchetypeAbility(models.Model):
    level = models.ForeignKey(ArchetypeLevel, on_delete=models.CASCADE,
                              related_name="archetype_abilities")
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class ArchetypeSpecificColumn(models.Model):
    archetype = models.ForeignKey(Archetype, on_delete=models.CASCADE,
                                  related_name="archetype_specific_columns")
    name = models.CharField(max_length=255)


class ArchetypeSpecificColumnValue(models.Model):
    specific_column = models.ForeignKey(ArchetypeSpecificColumn,
                                        on_delete=models.CASCADE,
                                        related_name="values")
    level = models.ForeignKey(ArchetypeLevel, on_delete=models.CASCADE,
                              related_name="specific_column_values")
    value = models.JSONField()


class ArchetypeCustomAbility(models.Model):
    character = models.ForeignKey('Character', on_delete=models.CASCADE,
                                  related_name='archetype_custom_abilities')
    ability = models.ForeignKey(ArchetypeAbility, on_delete=models.CASCADE,
                                related_name='archetype_custom_versions')
    custom_description = models.TextField(blank=True, null=True)
    hide_original = models.BooleanField(default=False)



