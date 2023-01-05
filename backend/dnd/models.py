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


class PreHistory(models.Model):
    history = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.history


class Race(models.Model):
    race = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.race

class WorldOutlook(models.Model):
    world_outlook = models.CharField(max_length=100, blank=True)
    def __str__(self):
        return self.world_outlook

class Character(models.Model):
    account = models.ForeignKey('auth.User', related_name='account',
                                on_delete=models.CASCADE)
    name_champion = models.CharField(max_length=100, blank=True,
                                     default='Безымянный герой')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    is_active = models.BooleanField(default=True)
    lvl = models.IntegerField(blank=True,default=1)
    spells = models.ManyToManyField(DndSpell,
                                    blank=True)
    champion_class = models.ForeignKey(BaseClassCh, on_delete=models.PROTECT,
                                       blank=True,null=True)
    pre_history = models.ForeignKey(PreHistory, on_delete=models.PROTECT,
                                    blank=True,null=True)
    race = models.ForeignKey(Race, on_delete=models.PROTECT, blank=True,null=True)
    world_outlook = models.ForeignKey(WorldOutlook, on_delete=models.PROTECT,
                                      blank=True,null=True)
    experience = models.IntegerField(blank=True, default=0)

    def __str__(self):
        return self.name_champion

    class Meta:
        verbose_name_plural = 'персонажи'
        verbose_name = 'пресонаж'
