from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver

from dnd.db.background import BackgroundModel
from dnd.db.character import BaseClass, Archetype
from dnd.db.inventory import Item
from dnd.db.lineament import LineamentModel
from dnd.db.origin import OriginModel
from dnd.db.race import Race, SubRace


class WorldOutlook(models.Model):
    name = models.CharField(max_length=100, blank=True)
    description = models.CharField(blank=True, null=True, max_length=4000)

    def __str__(self):
        return self.name


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


class Skills(models.Model):
    # характеристики
    strength = models.PositiveSmallIntegerField(verbose_name="Сила",
                                                blank=True, default=10)
    dexterity = models.PositiveSmallIntegerField(verbose_name="Ловкость",
                                                 blank=True, default=10)
    constitution = models.PositiveSmallIntegerField(
        verbose_name="Телосложение",
        blank=True, default=10)
    intelligence = models.PositiveSmallIntegerField(
        verbose_name="Интеллект",
        blank=True, default=10)
    wisdom = models.PositiveSmallIntegerField(verbose_name="Мудрость",
                                              blank=True, default=10)
    charisma = models.PositiveSmallIntegerField(verbose_name="Харизма",
                                                blank=True, default=10)

    def __str__(self):
        return f'{self.strength} {self.dexterity} {self.constitution} ' \
               f'{self.intelligence} {self.wisdom} {self.charisma}'

    @classmethod
    def default_skill(cls):
        created = cls.objects.create()
        return created.pk

class Lineament(models.Model):
    name = models.CharField(max_length=100, blank=True)
    description = models.CharField(blank=True, null=True, max_length=4000)

    def __str__(self):
        return self.name



class Character(models.Model):
    champion_class = models.ForeignKey(BaseClass,
                                       on_delete=models.SET_NULL,
                                       blank=True, null=True)
    archetype = models.ForeignKey(
        Archetype, on_delete=models.SET_NULL, blank=True, null=True,
        verbose_name="Архетип"
    )
    race = models.ForeignKey(Race, on_delete=models.PROTECT, blank=True,
                             null=True)
    sub_race = models.ForeignKey(SubRace, on_delete=models.PROTECT, blank=True,
                                 null=True)
    account = models.ForeignKey('auth.User', related_name='account',
                                on_delete=models.CASCADE)
    name_champion = models.CharField(max_length=100, blank=True,
                                     default='Безымянный герой')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    is_active = models.BooleanField(default=True)
    level = models.IntegerField(blank=True, default=1)

    spells = models.ManyToManyField(Spell,
                                    blank=True, related_name='my_spells')

    world_outlook = models.ForeignKey(WorldOutlook,
                                      on_delete=models.PROTECT,
                                      blank=True, null=True)
    experience = models.IntegerField(blank=True, default=0)
    protect_state = models.OneToOneField(
        ProtectStateModel,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name="Спасброски"
    )
    skill_state = models.OneToOneField(
        SkillStateModel,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name="Владения навыками"
    )
    skills = models.OneToOneField(
        Skills,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name="Характеристики"
    )
    max_hit = models.PositiveSmallIntegerField(default=0)
    temp_hit = models.PositiveSmallIntegerField(default=0)
    current_hit = models.PositiveSmallIntegerField(default=0)
    possession_bonus = models.PositiveSmallIntegerField(default=2,
                                                        verbose_name="bonus")
    inspiration = models.PositiveSmallIntegerField(default=0)

    protection_class = models.PositiveSmallIntegerField(default=10,
                                                        verbose_name="Класс защиты")
    speed = models.PositiveSmallIntegerField(default=30,
                                             verbose_name="speed_ch")
    lineament = models.ManyToManyField(LineamentModel, verbose_name="Черты",
                                       blank=True)
    origin = models.ForeignKey(OriginModel, blank=True, null=True,
                               on_delete=models.SET_NULL, verbose_name='Предыстория')

    def __str__(self):
        return self.name_champion

    def save(self, *args, **kwargs):
        # Если protect_state ещё не задан, создаём запись
        if not self.protect_state:
            self.protect_state = ProtectStateModel.objects.create()
        # Если skill_state ещё не задан, создаём запись
        if not self.skill_state:
            self.skill_state = SkillStateModel.objects.create()
        # Сохраняем объект Character
        if not self.skills:
            self.skills = Skills.objects.create()
        super().save(*args, **kwargs)

    def get_lineament(self):
        lineament_list = self.lineament.all()
        custom_map = {custom.lineament.id: custom for custom in
                      self.lineament_custom.all()}
        result = []
        for lineament in lineament_list:
            data = {
                'id': lineament.id,
                'name': lineament.name,
                'description': lineament.description,
            }
            custom = custom_map.get(lineament.id)
            if custom:
                data['custom'] = {
                    'id': custom.id,
                    'name': custom.custom_description,
                    'description': custom.hide_original,
                }
            result.append(data)
        return result

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
