from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver


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



class BaseClass(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название класса")
    description = models.TextField(verbose_name="Описание класса", blank=True,
                                   null=True)
    hit_dice = models.CharField(max_length=10, verbose_name="Кость хитов",
                                blank=True, null=True)
    hit_at_first_level = models.CharField(max_length=10, verbose_name="Хиты "
                                                                      "на "
                                                                      "первом уровне",
                                          blank=True, null=True)

    hit_at_next_level = models.CharField(max_length=100, verbose_name="Хиты "
                                                                      "на следующих уровнях",
                                         blank=True, null=True)
    possession_armor = models.CharField(max_length=100, verbose_name=
    "Владение доспехами", blank=True, null=True)
    possession_weapon = models.CharField(max_length=100, verbose_name=
    "Владение оружием", blank=True, null=True)
    possession_instrument = models.CharField(max_length=100,
                                             verbose_name="Владение инструментами",
                                             blank=True, null=True)
    saving_throws = models.CharField(max_length=100, verbose_name=
    "Спасброски", blank=True, null=True)

    class_skills = models.CharField(max_length=100, verbose_name=
    "Классовые навыки", blank=True, null=True)

    def __str__(self):
        return self.name

    def get_current_level_data(self, character_level):
        levels = self.levels.filter(level__lte=character_level).order_by(
            'level')

        abilities = {}
        for level in levels:
            level_abilities = [ability.name for ability in
                               level.abilities.all()]
            if level_abilities:
                abilities[str(level.level)] = level_abilities

        return {
            "level": character_level,
            "proficiency_bonus": levels.get(
                level=character_level).proficiency_bonus,
            "specific_columns": {
                column.name: column.values.get(level=character_level).value
                for column in self.specific_columns.all()
            },
            "abilities": abilities
        }


# ________Архетип__________

class Archetype(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название архетипа")
    character_class = models.ForeignKey(
        BaseClass, on_delete=models.CASCADE, related_name="archetypes",
        verbose_name="Класс"
    )
    description = models.TextField(
        verbose_name="Описание архетипа", blank=True, null=True
    )

    def get_current_level_data(self, character_level):
        levels = self.levels.filter(level__lte=character_level).order_by(
            'level')

        abilities = {}
        for level in levels:
            level_abilities = [ability.name for ability in
                               level.abilities.all()]
            if level_abilities:
                abilities[str(level.level)] = level_abilities

        specific_columns = {
            column.name: column.values.get(level=character_level).value
            for column in self.specific_columns.all()
        }

        return {
            # "level": character_level,
            "archetype_abilities": abilities,
            "archetype_specific_columns": specific_columns,
        }

    def __str__(self):
        return f"{self.name} ({self.character_class.name})"


class ArchetypeLevel(models.Model):
    archetype = models.ForeignKey(
        Archetype, on_delete=models.CASCADE, related_name="levels",
        verbose_name="Архетип"
    )
    level = models.PositiveIntegerField(verbose_name="Уровень")

    class Meta:
        unique_together = ("archetype", "level")
        ordering = ["archetype", "level"]

    def __str__(self):
        return f"{self.archetype.name} - Уровень {self.level}"


class ArchetypeAbility(models.Model):
    level = models.ForeignKey(
        ArchetypeLevel, on_delete=models.CASCADE, related_name="abilities",
        verbose_name="Уровень"
    )
    name = models.CharField(max_length=255, verbose_name="Название способности")
    description = models.TextField(
        verbose_name="Описание способности", max_length=500, blank=True,
        null=True
    )

    def __str__(self):
        return f"{self.name} ({self.level.archetype.name} - Уровень {self.level.level})"


class ArchetypeSpecificColumn(models.Model):
    archetype = models.ForeignKey(
        Archetype, on_delete=models.CASCADE, related_name="specific_columns",
        verbose_name="Архетип"
    )
    name = models.CharField(
        max_length=255, verbose_name="Название специфического столбца"
    )

    def __str__(self):
        return f"{self.name} ({self.archetype.name})"


class ArchetypeSpecificColumnValue(models.Model):
    specific_column = models.ForeignKey(
        ArchetypeSpecificColumn, on_delete=models.CASCADE,
        related_name="values",
        verbose_name="Специфический столбец"
    )
    level = models.ForeignKey(
        ArchetypeLevel, on_delete=models.CASCADE,
        related_name="specific_column_values", verbose_name="Уровень"
    )
    value = models.JSONField(verbose_name="Значение")

    class Meta:
        unique_together = ("specific_column", "level")

    def __str__(self):
        return (
            f"{self.specific_column.name} ({self.level.archetype.name} - "
            f"Уровень {self.level.level}): {self.value}"
        )


class Level(models.Model):
    class_obj = models.ForeignKey(BaseClass, on_delete=models.CASCADE,
                                  related_name="levels", verbose_name="Класс")
    level = models.PositiveIntegerField(verbose_name="Уровень")
    proficiency_bonus = models.PositiveIntegerField(
        verbose_name="Бонус мастерства")

    class Meta:
        unique_together = (
            "class_obj", "level")  # Уровень уникален в рамках класса
        ordering = ["class_obj", "level"]

    def __str__(self):
        return f"{self.class_obj.name} - Уровень {self.level}"


class Ability(models.Model):
    level = models.ForeignKey(Level, on_delete=models.CASCADE,
                              related_name="abilities", verbose_name="Уровень")
    name = models.CharField(max_length=255, verbose_name="Название способности")
    description = models.TextField(verbose_name="Описание способности",
                                   max_length=500, blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.level.class_obj.name} - Уровень {self.level.level})"


class SpecificColumn(models.Model):
    class_obj = models.ForeignKey(BaseClass, on_delete=models.CASCADE,
                                  related_name="specific_columns",
                                  verbose_name="Класс")
    name = models.CharField(max_length=255,
                            verbose_name="Название специфического столбца")

    def __str__(self):
        return f"{self.name} ({self.class_obj.name})"


class SpecificColumnValue(models.Model):
    specific_column = models.ForeignKey(SpecificColumn,
                                        on_delete=models.CASCADE,
                                        related_name="values",
                                        verbose_name="Специфический столбец")
    level = models.ForeignKey(Level, on_delete=models.CASCADE,
                              related_name="specific_column_values",
                              verbose_name="Уровень")
    value = models.JSONField(
        verbose_name="Значение")  # Хранение сложных данных (списков, словарей)

    class Meta:
        unique_together = (
            "specific_column",
            "level")  # Значение уникально для столбца и уровня

    def __str__(self):
        return f"{self.specific_column.name} ({self.level.class_obj.name} - Уровень {self.level.level}): {self.value}"


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


class FeatureRace(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название особенности")
    description = models.TextField(verbose_name="Описание особенности")

    class Meta:
        verbose_name = "Общие особенности расы"
        verbose_name_plural = "Общие особенности расы"

    def __str__(self):
        return self.name


class CustomFeature(models.Model):
    character = models.ForeignKey(
        'Character', on_delete=models.CASCADE, related_name='custom_features'
    )
    feature = models.ForeignKey(
        FeatureRace, on_delete=models.CASCADE, related_name='custom_features'
    )
    custom_description = models.TextField(
        verbose_name="Пользовательское описание", blank=True, null=True
    )
    hide_original = models.BooleanField(
        verbose_name="Скрыть оригинальный текст", default=False
    )

    class Meta:
        verbose_name = "Пользовательская общая особенность расы"
        verbose_name_plural = "Пользовательские общие особенности рас"

    def __str__(self):
        return f"{self.character.name_champion} - {self.feature.name}"


class RaceBackground(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название особенности")
    description = models.TextField(verbose_name="Описание особенности")

    class Meta:
        verbose_name = "Историческая особенность расы"
        verbose_name_plural = "Исторические особенности рас"

    def __str__(self):
        return self.name


class CustomRaceBackground(models.Model):
    character = models.ForeignKey(
        'Character', on_delete=models.CASCADE, related_name='custom_history_race_backgrounds'
    )
    race_background = models.ForeignKey(
        RaceBackground, on_delete=models.CASCADE,
        related_name='custom_history_race_backgrounds',
    )
    custom_description = models.TextField(
        verbose_name="Пользовательское описание", blank=True, null=True
    )
    hide_original = models.BooleanField(
        verbose_name="Скрыть оригинальный текст", default=False
    )

    class Meta:
        verbose_name = "Пользовательская историческая особенность расы"
        verbose_name_plural = "Пользовательские исторические особенности рас"

    def __str__(self):
        return f"{self.character.name_champion} - {self.race_background.name}"


class Race(models.Model):
    name = models.CharField(max_length=50, unique=True,
                            verbose_name="Название расы")
    description = models.TextField(verbose_name="Описание")
    background = models.ManyToManyField(RaceBackground, verbose_name="История "
                                                                 "рассы",
                                    related_name='races_backgrounds', )
    features = models.ManyToManyField(
        FeatureRace,
        related_name="races_features",
        verbose_name="Особенности"
    )

    class Meta:
        verbose_name = "Раса"
        verbose_name_plural = "Расы"

    def __str__(self):
        return self.name


class SubRace(models.Model):
    race = models.ForeignKey(
        Race,
        on_delete=models.CASCADE,
        related_name="subraces",
        verbose_name="Основная раса"
    )
    name = models.CharField(max_length=100, verbose_name="Название подвида")
    description = models.TextField(verbose_name="Описание")
    background = models.ManyToManyField(RaceBackground, verbose_name="История подвида",
                                    related_name='sub_races_backgrounds')
    features = models.ManyToManyField(
        FeatureRace,
        related_name="sub_races_features_race",
        verbose_name="Особенности подвида"
    )

    class Meta:
        verbose_name = "Подвид"
        verbose_name_plural = "Подвиды"

    def __str__(self):
        return f"{self.name} ({self.race.name})"


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
            current_level)

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
