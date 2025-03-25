from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Spell(models.Model):
    link = models.CharField(max_length=100, verbose_name='ссылка')
    name = models.CharField(max_length=100, verbose_name='название')
    school = models.CharField(max_length=60, verbose_name='школа')
    time_cast = models.CharField(max_length=200,
                                 verbose_name='время накладывания')
    distance = models.CharField(max_length=100, verbose_name='дистанция')
    components = models.CharField(max_length=400, verbose_name='компоненты')
    timing = models.CharField(max_length=100, verbose_name='Длительность')
    class_actor = models.ManyToManyField('BaseClass',
                                         related_name="class_spells",
                                         blank=True)
    archetype = models.ManyToManyField('Archetype',
                                       related_name='archetype_spells',
                                       blank=True)
    origin = models.CharField(blank=True, null=True, max_length=100,
                              verbose_name='источник')
    instruction = models.TextField(verbose_name='описание')
    level = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(9)], blank=True)

    class Meta:
        verbose_name_plural = 'Заклинания'
        verbose_name = 'Заклинание'
        ordering = ['level', 'name']

    def __str__(self):
        return self.name + ' ' + str(self.level)


class SpellSlotLevel(models.Model):
    level = models.PositiveIntegerField(unique=True, default=0, validators=[
        MaxValueValidator(9), MinValueValidator(0)])
    count = models.PositiveIntegerField(default=0, validators=[
        MaxValueValidator(12), MinValueValidator(0)])
    used = models.PositiveIntegerField(default=0, validators=[
        MaxValueValidator(12), MinValueValidator(0)])

    class Meta:
        verbose_name = 'Уровень ячеек заклинаний'
        verbose_name_plural = 'Уровни ячеек заклинаний'


    def __str__(self):
        return f"Level {self.level}: Count={self.count}, Used={self.used}"


class CharacterSpellSlots(models.Model):
    character = models.OneToOneField(
        'Character',  # Предполагается, что есть модель Character
        on_delete=models.CASCADE,
        related_name='spell_slots',
        verbose_name='Персонаж'
    )
    levels = models.ManyToManyField(
        SpellSlotLevel,
        through='CharacterSpellSlotLevel',
        verbose_name='Уровни ячеек'
    )

    class Meta:
        verbose_name = 'Ячейки заклинаний персонажа'
        verbose_name_plural = 'Ячейки заклинаний персонажей'

    def __str__(self):
        return f"Ячейки заклинаний для {self.character}"




class CharacterSpellSlotLevel(models.Model):
    character_spell_slots = models.ForeignKey(
        CharacterSpellSlots,
        on_delete=models.CASCADE,
        related_name='slot_levels',
        verbose_name='Ячейки заклинаний персонажа'
    )
    spell_slot_level = models.ForeignKey(
        SpellSlotLevel,
        on_delete=models.CASCADE,
        related_name='character_slots',
        verbose_name='Уровень ячейки'
    )
    spells = models.JSONField(default=list, blank=True,null=True)

    class Meta:
        verbose_name = 'Уровень ячеек заклинаний персонажа'
        verbose_name_plural = 'Уровни ячеек заклинаний персонажей'

    def __str__(self):
        return f"{self.character_spell_slots.character} - Уровень {self.spell_slot_level.level}"