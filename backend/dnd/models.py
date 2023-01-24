from django.db import models


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

    def __str__(self):
        return self.name

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


class BackgroundModel(models.Model):
    personality_traits = models.CharField(max_length=1500, blank=True,
                                          default='черты характера')
    ideals = models.CharField(max_length=1500, blank=True,
                              default="идеалы")
    bonds = models.CharField(max_length=1500, blank=True,
                             default="узы")
    flaws = models.CharField(max_length=1500, blank=True,
                             default="недостатки")

    @classmethod
    def default_background(cls):
        return cls.objects.get_or_create()


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
                                    blank=True)
    champion_class = models.ForeignKey(BaseClassCh,
                                       on_delete=models.PROTECT,
                                       blank=True, null=True)
    race = models.ForeignKey(Race, on_delete=models.PROTECT, blank=True,
                             null=True)
    world_outlook = models.ForeignKey(WorldOutlook,
                                      on_delete=models.PROTECT,
                                      blank=True, null=True)
    experience = models.IntegerField(blank=True, default=0)

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
    pre_history = models.ForeignKey(PreHistoryModel,
                                    verbose_name="pre_history_champ",
                                    on_delete=models.CASCADE,
                                    blank=True, null=True)
    background = models.ForeignKey(BackgroundModel,
                                   on_delete=models.CASCADE,
                                   default=BackgroundModel.default_background,
                                   related_name='bac')

    def __str__(self):
        return self.name_champion

    class Meta:
        verbose_name_plural = 'персонажи'
        verbose_name = 'пресонаж'
