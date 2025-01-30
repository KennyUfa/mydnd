from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver

from dnd.db.champion_class import Archetype, BaseClass
from dnd.db.inventory import Item
from dnd.db.race import Race, SubRace


class WorldOutlook(models.Model):
    name = models.CharField(max_length=100, blank=True)
    description = models.CharField(blank=True, null=True, max_length=4000)

    def __str__(self):
        return self.name


class Ideal(models.Model):
    choice = models.CharField(max_length=100)

    def __str__(self):
        return self.choice


class ProtectStateModel(models.Model):
    protect_state_strength = models.IntegerField(default=1, validators=[
        MaxValueValidator(2), MinValueValidator(1)])
    protect_state_dexterity = models.IntegerField(default=1, validators=[
        MaxValueValidator(2), MinValueValidator(1)])
    protect_state_constitution = models.IntegerField(default=1, validators=[
        MaxValueValidator(2), MinValueValidator(1)])
    protect_state_intelligence = models.IntegerField(default=1, validators=[
        MaxValueValidator(2), MinValueValidator(1)])
    protect_state_wisdom = models.IntegerField(default=1, validators=[
        MaxValueValidator(2), MinValueValidator(1)])
    protect_state_charisma = models.IntegerField(default=1, validators=[
        MaxValueValidator(2), MinValueValidator(1)])

    @classmethod
    def default_protect_state(cls):
        created = cls.objects.create()
        return created.pk


class SkillStateModel(models.Model):
    athletics = models.IntegerField(default=1, validators=[
        MaxValueValidator(3), MinValueValidator(1)])
    acrobatics = models.IntegerField(default=1, validators=[
        MaxValueValidator(3), MinValueValidator(1)])
    sleight_of_hand = models.IntegerField(default=1, validators=[
        MaxValueValidator(3), MinValueValidator(1)])
    stealth = models.IntegerField(default=1, validators=[
        MaxValueValidator(3), MinValueValidator(1)])
    arcana = models.IntegerField(default=1, validators=[
        MaxValueValidator(3), MinValueValidator(1)])
    history = models.IntegerField(default=1, validators=[
        MaxValueValidator(3), MinValueValidator(1)])
    investigation = models.IntegerField(default=1, validators=[
        MaxValueValidator(3), MinValueValidator(1)])
    nature = models.IntegerField(default=1, validators=[
        MaxValueValidator(3), MinValueValidator(1)])
    religion = models.IntegerField(default=1, validators=[
        MaxValueValidator(3), MinValueValidator(1)])
    animal_handling = models.IntegerField(default=1, validators=[
        MaxValueValidator(3), MinValueValidator(1)])
    insight = models.IntegerField(default=1, validators=[
        MaxValueValidator(3), MinValueValidator(1)])
    medicine = models.IntegerField(default=1, validators=[
        MaxValueValidator(3), MinValueValidator(1)])
    perception = models.IntegerField(default=1, validators=[
        MaxValueValidator(3), MinValueValidator(1)])
    survival = models.IntegerField(default=1, validators=[
        MaxValueValidator(3), MinValueValidator(1)])
    deception = models.IntegerField(default=1, validators=[
        MaxValueValidator(3), MinValueValidator(1)])
    intimidation = models.IntegerField(default=1, validators=[
        MaxValueValidator(3), MinValueValidator(1)])
    performance = models.IntegerField(default=1, validators=[
        MaxValueValidator(3), MinValueValidator(1)])
    persuasion = models.IntegerField(default=1, validators=[
        MaxValueValidator(3), MinValueValidator(1)])

    @classmethod
    def default_skill_state(cls):
        created = cls.objects.create()
        return created.pk


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
    class_actor = models.ManyToManyField(BaseClass,
                                         related_name="class_spells",
                                         blank=True)
    archetype = models.ManyToManyField(Archetype,
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


class BackgroundModel(models.Model):
    personality_traits = models.CharField(max_length=1500,
                                          default='черты характера')
    ideals = models.CharField(max_length=1500,
                              default="идеалы")
    bonds = models.CharField(max_length=1500,
                             default="узы")
    flaws = models.CharField(max_length=1500,
                             default="недостатки")


class Character(models.Model):
    champion_class = models.ForeignKey(BaseClass,
                                       on_delete=models.PROTECT,
                                       blank=True, null=True)
    archetype = models.ForeignKey(
        Archetype, on_delete=models.PROTECT, blank=True, null=True,
        verbose_name="Архетип"
    )
    race = models.ForeignKey(Race, on_delete=models.PROTECT, blank=True,
                             null=True)
    sub_race = models.ForeignKey(SubRace, on_delete=models.PROTECT, blank=True,
                                 null=True)
    background = models.ForeignKey(BackgroundModel, on_delete=models.CASCADE, )
    account = models.ForeignKey('auth.User', related_name='account',
                                on_delete=models.CASCADE,
                                default='settings.AUTH_USER_MODEL')
    name_champion = models.CharField(max_length=100, blank=True,
                                     default='Безымянный герой')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    is_active = models.BooleanField(default=True)
    lvl = models.IntegerField(blank=True, default=1)

    spells = models.ManyToManyField(Spell,
                                    blank=True, related_name='my_spells')

    world_outlook = models.OneToOneField(WorldOutlook,
                                         on_delete=models.PROTECT,
                                         blank=True, null=True)
    experience = models.IntegerField(blank=True, default=0)
    protect_state = models.OneToOneField(
        ProtectStateModel,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    skill_state = models.OneToOneField(
        SkillStateModel,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    ProficienciesAndLanguages = models.CharField(max_length=4000,
                                                 default="Список навыков и языков")

    max_hit = models.PositiveSmallIntegerField(default=0)
    temp_hit = models.PositiveSmallIntegerField(default=0)
    current_hit = models.PositiveSmallIntegerField(default=0)

    # характеристики
    strength = models.PositiveSmallIntegerField(verbose_name="Сила",
                                                blank=True, default=10)
    dexterity = models.PositiveSmallIntegerField(verbose_name="Ловкость",
                                                 blank=True, default=10)
    constitution = models.PositiveSmallIntegerField(
        verbose_name="Телосложение",
        blank=True, default=10)
    intelligence = models.PositiveSmallIntegerField(
        verbose_name="Интиллект",
        blank=True, default=10)
    wisdom = models.PositiveSmallIntegerField(verbose_name="Мудрость",
                                              blank=True, default=10)
    charisma = models.PositiveSmallIntegerField(verbose_name="Харизма",
                                                blank=True, default=10)
    possession_bonus = models.PositiveSmallIntegerField(default=2,
                                                        verbose_name="bonus")
    inspiration = models.PositiveSmallIntegerField(default=0)

    protection_class = models.PositiveSmallIntegerField(default=10,
                                                        verbose_name="kz")
    speed = models.PositiveSmallIntegerField(default=30,
                                             verbose_name="speed_ch")

    def __str__(self):
        return self.name_champion

    def get_current_level_data(self):
        current_level = self.lvl
        base_class_data = self.champion_class.get_current_level_data(
            current_level,self)

        if self.archetype:
            archetype_data = self.archetype.get_current_level_data(
                current_level)

        return base_class_data, archetype_data

    def save(self, *args, **kwargs):
        # Если protect_state ещё не задан, создаём запись
        if not self.protect_state:
            self.protect_state = ProtectStateModel.objects.create()
        # Если skill_state ещё не задан, создаём запись
        if not self.skill_state:
            self.skill_state = SkillStateModel.objects.create()
        # Сохраняем объект Character
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'персонажи'
        verbose_name = 'пресонаж'


class InventoryItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    character = models.ForeignKey(Character, on_delete=models.CASCADE,
                                  related_name='my_items')
    quantity = models.PositiveIntegerField(default=1)


# эти записи не удалялись при удалении персонажа, поправил таким костылем
@receiver(post_delete, sender=Character)
def delete_related_states(sender, instance, **kwargs):
    if instance.protect_state:
        instance.protect_state.delete()
    if instance.skill_state:
        instance.skill_state.delete()
