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


class Archetype(models.Model):
    name = models.CharField(max_length=100)
    character_class = models.ForeignKey(BaseClass, on_delete=models.CASCADE,
                                        related_name="archetypes")
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Level(models.Model):
    class_obj = models.ForeignKey(BaseClass, on_delete=models.CASCADE,
                                  related_name="levels", blank=True, null=True)
    archetype = models.ForeignKey(Archetype,related_name="levels", on_delete=models.CASCADE,
                                  blank=True, null=True)

    level = models.PositiveIntegerField()
    proficiency_bonus = models.PositiveIntegerField()

    def __str__(self):
        return str(f"{self.class_obj} {self.archetype.name if self.archetype else ''} - {self.level}")


class Ability(models.Model):
    level_id = models.ForeignKey(Level, on_delete=models.CASCADE,
                              related_name="abilities")
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class CustomAbility(models.Model):
    character = models.ForeignKey('Character', on_delete=models.CASCADE,
                                  related_name='custom_abilities')
    ability = models.ForeignKey(Ability, on_delete=models.CASCADE,
                                related_name='custom_versions')
    custom_description = models.TextField(blank=True, null=True)
    hide_original = models.BooleanField(default=False)
    hide_custom = models.BooleanField(default=True)


class SpecificColumn(models.Model):
    level = models.ForeignKey(Level, on_delete=models.CASCADE,
                              related_name="specific_column")
    class_obj = models.ForeignKey(BaseClass, on_delete=models.CASCADE,
                                  related_name="specific_columns")
    name = models.CharField(max_length=255)
    value = models.CharField(max_length=10)

class SpellSlot(models.Model):
    level = models.ForeignKey(Level, on_delete=models.CASCADE,
                              related_name="spell_slots")
    slots = models.JSONField()