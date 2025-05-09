from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
from background.models import Background
from champion_class.models import Archetype, BaseClass
from lineaments.models import LineamentModel
from race.models import Race, SubRace
from spellbook.models import CharacterSpellSlots, SpellSlotLevel, CharacterSpellSlotLevel
from worldoutlook.models import WorldOutlook


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

class Character(models.Model):
    champion_class = models.ForeignKey(BaseClass,
                                       on_delete=models.SET_NULL,
                                       blank=True, null=True)
    archetype = models.ForeignKey(
        Archetype, on_delete=models.SET_NULL, blank=True, null=True,
        verbose_name="Архетип"
    )
    race = models.ForeignKey(Race, on_delete=models.SET_NULL, blank=True,
                             null=True)
    sub_race = models.ForeignKey(SubRace, on_delete=models.SET_NULL, blank=True,
                                 null=True)
    account = models.ForeignKey('auth.User', related_name='account',
                                on_delete=models.CASCADE)
    name_champion = models.CharField(max_length=100, blank=True,
                                     default='Безымянный герой')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    is_active = models.BooleanField(default=True)
    level = models.IntegerField(blank=True, default=1)
    world_outlook = models.ForeignKey(WorldOutlook,
                                      on_delete=models.SET_NULL,
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
    background = models.ForeignKey(Background, blank=True, null=True,
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
        # Если skills ещё не задан, создаём запись
        if not self.skills:
            self.skills = Skills.objects.create()
        super().save(*args, **kwargs)
        if not hasattr(self, 'spell_slots'):
            try:
                # Создаем CharacterSpellSlots для персонажа при первом сохранении
                character_spell_slots = CharacterSpellSlots.objects.create(character=self)

                # Создаем стандартные уровни ячеек заклинаний
                for level in range(0, 10):  # Уровни от 0 до 9
                    spell_slot_level = SpellSlotLevel.objects.create(
                        level=level,
                        count=0,
                        used=0
                    )

                    # Создаем связь между персонажем и уровнем ячеек
                    CharacterSpellSlotLevel.objects.create(
                        character_spell_slots=character_spell_slots,
                        spell_slot_level=spell_slot_level
                    )
            except Exception as e:
                print(f"Ошибка создания ячеек заклинаний: {e}")

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


# эти записи не удалялись при удалении персонажа, поправил таким костылем
@receiver(post_delete, sender=Character)
def delete_related_states(sender, instance, **kwargs):
    if instance.protect_state:
        instance.protect_state.delete()
    if instance.skill_state:
        instance.skill_state.delete()
    if instance.skills:
        instance.skills.delete()