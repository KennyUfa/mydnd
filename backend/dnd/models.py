from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


# Общий инвентарь
class Properties(models.Model):
    name = models.CharField(blank=True, null=True, max_length=200, default='')
    description = models.CharField(blank=True, null=True, max_length=2000,
                                   default='')

    def __str__(self):
        return self.name


class TypeItem(models.Model):
    description = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.description


class Rarity(models.Model):
    description = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.description


class Item(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True, )
    type = models.ForeignKey(TypeItem, on_delete=models.CASCADE, blank=True)
    rarity = models.ForeignKey(Rarity, on_delete=models.CASCADE, blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


# Оружие
class SubType(models.Model):
    description = models.CharField(blank=True, null=True, max_length=200)

    def __str__(self):
        return self.description


class Weapon(models.Model):
    item = models.OneToOneField(Item, on_delete=models.CASCADE,
                                related_name='weapon')
    homebrew = models.BooleanField(default=False)
    type = models.ForeignKey(SubType, on_delete=models.CASCADE, blank=True,
                             null=True)
    damage = models.CharField(blank=True, null=True, max_length=10)
    damage_type = models.CharField(blank=True, null=True, max_length=200)
    price = models.CharField(blank=True, null=True, max_length=200)
    weight = models.CharField(blank=True, null=True, max_length=100, default='')
    properties = models.ManyToManyField(Properties, blank=True)
    source = models.CharField(blank=True, null=True, max_length=200)
    description = models.CharField(blank=True, null=True, max_length=3000)
    special = models.CharField(blank=True, null=True, max_length=3000)

    def __str__(self):
        return self.item.name


class Armor(models.Model):
    item = models.OneToOneField(Item, on_delete=models.CASCADE,
                                related_name='armor')
    sub_type = models.ForeignKey(SubType, on_delete=models.CASCADE, blank=True,
                                 null=True, related_name='armor')
    homebrew = models.BooleanField(default=False)
    disadvantage = models.BooleanField(default=False)

    armore = models.CharField(blank=True, null=True, max_length=100)
    duration = models.CharField(blank=True, null=True, max_length=100)
    price = models.CharField(blank=True, null=True, max_length=200)
    weight = models.CharField(blank=True, null=True, max_length=100, default='')
    source = models.CharField(blank=True, null=True, max_length=200)
    description = models.CharField(blank=True, null=True, max_length=3000)
    requirement = models.CharField(blank=True, null=True, max_length=10)

    def __str__(self):
        return self.item.name


class Equipment(models.Model):
    item = models.OneToOneField(Item, on_delete=models.CASCADE,
                                related_name='equipment')
    sub_type = models.ForeignKey(SubType, on_delete=models.CASCADE, blank=True,
                                 null=True, related_name='equipment')
    homebrew = models.BooleanField(default=False)
    price = models.CharField(blank=True, null=True, max_length=200, default='-')
    source = models.CharField(blank=True, null=True, max_length=200,
                              default='-')
    weight = models.CharField(blank=True, null=True, max_length=100,
                              default='-')
    description = models.CharField(blank=True, null=True, max_length=3000,
                                   default='-')

    def __str__(self):
        return self.item.name


class MagicItems(models.Model):
    item = models.OneToOneField(Item, on_delete=models.CASCADE,
                                related_name='magic_item')
    sub_type = models.ForeignKey(SubType, on_delete=models.CASCADE, blank=True,
                                 null=True, related_name='magic_item_type')
    homebrew = models.BooleanField(default=False)
    price = models.CharField(blank=True, null=True, max_length=200, default='-')
    source = models.CharField(blank=True, null=True, max_length=200,
                              default='-')

    customization = models.BooleanField(default=False)
    description = models.CharField(blank=True, null=True, max_length=3000,
                                   default='-')
    detailCustamization = models.CharField(blank=True, null=True,
                                           max_length=200,
                                           default='-')

    detailType = models.CharField(blank=True, null=True, max_length=200,
                                  default='-')

    def __str__(self):
        return self.item.name


class DndSpell(models.Model):
    link = models.CharField(max_length=100, verbose_name='ссылка')
    name = models.CharField(max_length=100, verbose_name='название')
    lvl = models.CharField(max_length=15, verbose_name='уровень')
    school = models.CharField(max_length=60, verbose_name='школа')
    time_cast = models.CharField(max_length=200,
                                 verbose_name='время накладывания')
    distance = models.CharField(max_length=100, verbose_name='дистанция')
    components = models.CharField(max_length=400, verbose_name='компоненты')
    timing = models.CharField(max_length=100, verbose_name='Длительность')
    class_actor = models.CharField(max_length=150, verbose_name='Классы',
                                   blank=True, null=True)
    architype = models.CharField(max_length=200, verbose_name='Архетипы',
                                 blank=True, null=True)
    origin = models.CharField(blank=True, null=True, max_length=100,
                              verbose_name='источник')
    instruction = models.TextField(verbose_name='описание')

    class Meta:
        verbose_name_plural = 'Заклинания'
        verbose_name = 'Заклинание'


class BaseClassCh(models.Model):
    champion_class = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.champion_class


class Race(models.Model):
    race = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.race


class WorldOutlook(models.Model):
    world_outlook = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.world_outlook


class PreHistoryModel(models.Model):
    pre_history_choices = models.CharField(max_length=100, blank=True,
                                           null=True)

    def __str__(self):
        return self.pre_history_choices


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


class BackgroundModel(models.Model):
    personality_traits = models.CharField(max_length=1500,
                                          default='черты характера')
    ideals = models.CharField(max_length=1500,
                              default="идеалы")
    bonds = models.CharField(max_length=1500,
                             default="узы")
    flaws = models.CharField(max_length=1500,
                             default="недостатки")

    @classmethod
    def default(cls):
        created = cls.objects.create()
        return created.pk


class Character(models.Model):
    account = models.ForeignKey('auth.User', related_name='account',
                                on_delete=models.CASCADE,
                                default='settings.AUTH_USER_MODEL')
    name_champion = models.CharField(max_length=100, blank=True,
                                     default='Безымянный герой')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    is_active = models.BooleanField(default=True)
    lvl = models.IntegerField(blank=True, default=1)
    spells = models.ManyToManyField(DndSpell,
                                    blank=True, related_name='my_spells')
    champion_class = models.ForeignKey(BaseClassCh,
                                       on_delete=models.PROTECT,
                                       blank=True, null=True)
    race = models.ForeignKey(Race, on_delete=models.PROTECT, blank=True,
                             null=True)
    world_outlook = models.ForeignKey(WorldOutlook,
                                      on_delete=models.PROTECT,
                                      blank=True, null=True)
    experience = models.IntegerField(blank=True, default=0)
    protect_char_state = models.ForeignKey(ProtectStateModel,
                                           on_delete=models.CASCADE,
                                           default=ProtectStateModel.default_protect_state)
    skill_char_state = models.ForeignKey(SkillStateModel,
                                         on_delete=models.CASCADE,
                                         default=SkillStateModel.default_skill_state)
    background = models.ForeignKey(BackgroundModel,
                                   on_delete=models.CASCADE,
                                   default=BackgroundModel.default)
    pre_history = models.ForeignKey(PreHistoryModel, on_delete=models.PROTECT,
                                    blank=True, null=True)
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

    class Meta:
        verbose_name_plural = 'персонажи'
        verbose_name = 'пресонаж'


class Inventory(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE,
                                  related_name='inventory')
    item = models.ForeignKey(Item, on_delete=models.CASCADE,related_name='inventory')
    quantity = models.IntegerField(default=1)
