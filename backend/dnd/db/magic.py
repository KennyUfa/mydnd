from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Spell(models.Model):
    link = models.CharField(max_length=100, verbose_name='ссылка')
    name = models.CharField(max_length=100, verbose_name='название')
    lvl = models.CharField(max_length=15, verbose_name='уровень')
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

    class Meta:
        verbose_name_plural = 'Заклинания'
        verbose_name = 'Заклинание'
        ordering = ['name']

    def __str__(self):
        return self.name


class SpellSlotLevel(models.Model):
    level = models.PositiveIntegerField(unique=True, default=0, validators=[
        MaxValueValidator(9), MinValueValidator(0)])
    count = models.PositiveIntegerField(default=0, validators=[
        MaxValueValidator(12), MinValueValidator(0)])
    used = models.PositiveIntegerField(default=0, validators=[
        MaxValueValidator(12), MinValueValidator(0)])

    def __str__(self):
        return f"Level {self.level}: Count={self.count}, Used={self.used}"


class CharacterSpellSlots(models.Model):
    character = models.OneToOneField(
        'Character',  # Предполагается, что есть модель Character
        on_delete=models.CASCADE,
        related_name='spell_slots'
    )
    levels = models.ManyToManyField(SpellSlotLevel, through='CharacterSpellSlotLevel')


class CharacterSpellSlotLevel(models.Model):
    character_spell_slots = models.ForeignKey(CharacterSpellSlots, on_delete=models.CASCADE)
    spell_slot_level = models.ForeignKey(SpellSlotLevel, on_delete=models.CASCADE)
    spells = models.ManyToManyField(Spell, blank=True)

    def __str__(self):
        return f"Character {self.character_spell_slots.character} - Level {self.spell_slot_level.level}"
