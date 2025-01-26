from django.db import migrations

def populate_bard_data(apps, schema_editor):
    # Получаем модели
    Class = apps.get_model('dnd', 'BaseClass')
    Level = apps.get_model('dnd', 'Level')
    Ability = apps.get_model('dnd', 'Ability')
    SpecificColumn = apps.get_model('dnd', 'SpecificColumn')
    SpecificColumnValue = apps.get_model('dnd', 'SpecificColumnValue')

    # Получаем существующий класс "Бард"
    bard, created = Class.objects.get_or_create(
        name="бард",
        defaults={
            "description": "Мастер вдохновения, магии и искусства."
        }
    )

    # Если класс уже существует, обновляем его описание (опционально)
    if not created:
        bard.description = "Мастер вдохновения, магии и искусства."
        bard.save()

    # Создаем специфические столбцы для Барда (если их еще нет)
    known_cantrips, _ = SpecificColumn.objects.get_or_create(
        class_obj=bard,
        name="Известные заговоры"
    )

    known_spells, _ = SpecificColumn.objects.get_or_create(
        class_obj=bard,
        name="Известные заклинания"
    )

    spell_slots, _ = SpecificColumn.objects.get_or_create(
        class_obj=bard,
        name="Ячейки заклинаний на уровень заклинаний"
    )

    # Данные для Барда (1-20 уровни)
    bard_data = [
        {
            "level": 1,
            "proficiency_bonus": 2,
            "abilities": ["Вдохновение барда", "Магическое воззвание"],
            "known_cantrips": 2,
            "known_spells": 4,
            "spell_slots": {"1": 2}
        },
        {
            "level": 2,
            "proficiency_bonus": 2,
            "abilities": ["Песнь отдыха"],
            "known_cantrips": 2,
            "known_spells": 5,
            "spell_slots": {"1": 3}
        },
        {
            "level": 3,
            "proficiency_bonus": 2,
            "abilities": ["Колледж барда"],
            "known_cantrips": 2,
            "known_spells": 6,
            "spell_slots": {"1": 4, "2": 2}
        },
        # ... (продолжите для всех уровней до 20)
        {
            "level": 20,
            "proficiency_bonus": 6,
            "abilities": ["Верховное вдохновение"],
            "known_cantrips": 4,
            "known_spells": 22,
            "spell_slots": {"1": 4, "2": 3, "3": 3, "4": 3, "5": 3, "6": 2,
                            "7": 2, "8": 1, "9": 1}
        },
        # Уровень 4
        {
            "level": 4,
            "proficiency_bonus": 2,
            "abilities": ["Увеличение характеристик"],
            "known_cantrips": 3,
            "known_spells": 7,
            "spell_slots": {"1": 4, "2": 3}
        },
        # Уровень 5
        {
            "level": 5,
            "proficiency_bonus": 3,
            "abilities": ["Вдохновение барда (улучшение)",
                          "Источник вдохновения"],
            "known_cantrips": 3,
            "known_spells": 8,
            "spell_slots": {"1": 4, "2": 3, "3": 2}
        },
        # Уровень 6
        {
            "level": 6,
            "proficiency_bonus": 3,
            "abilities": ["Магические секреты"],
            "known_cantrips": 3,
            "known_spells": 9,
            "spell_slots": {"1": 4, "2": 3, "3": 3}
        },
        # Уровень 7
        {
            "level": 7,
            "proficiency_bonus": 3,
            "abilities": [],
            "known_cantrips": 3,
            "known_spells": 10,
            "spell_slots": {"1": 4, "2": 3, "3": 3, "4": 1}
        },
        # Уровень 8
        {
            "level": 8,
            "proficiency_bonus": 3,
            "abilities": ["Увеличение характеристик"],
            "known_cantrips": 3,
            "known_spells": 11,
            "spell_slots": {"1": 4, "2": 3, "3": 3, "4": 2}
        },
        # Уровень 9
        {
            "level": 9,
            "proficiency_bonus": 4,
            "abilities": ["Песнь отдыха (улучшение)"],
            "known_cantrips": 3,
            "known_spells": 12,
            "spell_slots": {"1": 4, "2": 3, "3": 3, "4": 3, "5": 1}
        },
        # Уровень 10
        {
            "level": 10,
            "proficiency_bonus": 4,
            "abilities": ["Магические секреты", "Экспертиза"],
            "known_cantrips": 4,
            "known_spells": 14,
            "spell_slots": {"1": 4, "2": 3, "3": 3, "4": 3, "5": 2}
        },
        # Уровень 11
        {
            "level": 11,
            "proficiency_bonus": 4,
            "abilities": [],
            "known_cantrips": 4,
            "known_spells": 15,
            "spell_slots": {"1": 4, "2": 3, "3": 3, "4": 3, "5": 2, "6": 1}
        },
        # Уровень 12
        {
            "level": 12,
            "proficiency_bonus": 4,
            "abilities": ["Увеличение характеристик"],
            "known_cantrips": 4,
            "known_spells": 15,
            "spell_slots": {"1": 4, "2": 3, "3": 3, "4": 3, "5": 2, "6": 1}
        },
        # Уровень 13
        {
            "level": 13,
            "proficiency_bonus": 5,
            "abilities": ["Песнь отдыха (улучшение)"],
            "known_cantrips": 4,
            "known_spells": 16,
            "spell_slots": {"1": 4, "2": 3, "3": 3, "4": 3, "5": 2, "6": 1,
                            "7": 1}
        },
        # Уровень 14
        {
            "level": 14,
            "proficiency_bonus": 5,
            "abilities": ["Магические секреты"],
            "known_cantrips": 4,
            "known_spells": 18,
            "spell_slots": {"1": 4, "2": 3, "3": 3, "4": 3, "5": 2, "6": 1,
                            "7": 1}
        },
        # Уровень 15
        {
            "level": 15,
            "proficiency_bonus": 5,
            "abilities": [],
            "known_cantrips": 4,
            "known_spells": 19,
            "spell_slots": {"1": 4, "2": 3, "3": 3, "4": 3, "5": 2, "6": 1,
                            "7": 1, "8": 1}
        },
        # Уровень 16
        {
            "level": 16,
            "proficiency_bonus": 5,
            "abilities": ["Увеличение характеристик"],
            "known_cantrips": 4,
            "known_spells": 19,
            "spell_slots": {"1": 4, "2": 3, "3": 3, "4": 3, "5": 2, "6": 1,
                            "7": 1, "8": 1}
        },
        # Уровень 17
        {
            "level": 17,
            "proficiency_bonus": 6,
            "abilities": ["Песнь отдыха (улучшение)"],
            "known_cantrips": 4,
            "known_spells": 20,
            "spell_slots": {"1": 4, "2": 3, "3": 3, "4": 3, "5": 2, "6": 1,
                            "7": 1, "8": 1, "9": 1}
        },
        # Уровень 18
        {
            "level": 18,
            "proficiency_bonus": 6,
            "abilities": ["Магические секреты"],
            "known_cantrips": 4,
            "known_spells": 22,
            "spell_slots": {"1": 4, "2": 3, "3": 3, "4": 3, "5": 3, "6": 1,
                            "7": 1, "8": 1, "9": 1}
        },
        # Уровень 19
        {
            "level": 19,
            "proficiency_bonus": 6,
            "abilities": ["Увеличение характеристик"],
            "known_cantrips": 4,
            "known_spells": 22,
            "spell_slots": {"1": 4, "2": 3, "3": 3, "4": 3, "5": 3, "6": 2,
                            "7": 1, "8": 1, "9": 1}
        },
    ]

    # Заполняем данные
    for data in bard_data:
        # Проверяем, существует ли уже уровень
        level_obj, created = Level.objects.get_or_create(
            class_obj=bard,
            level=data["level"],
            defaults={
                "proficiency_bonus": data["proficiency_bonus"]
            }
        )

        # Если уровень уже существует, обновляем proficiency_bonus (опционально)
        if not created:
            level_obj.proficiency_bonus = data["proficiency_bonus"]
            level_obj.save()

        # Добавляем умения (если их еще нет)
        for ability_name in data["abilities"]:
            Ability.objects.get_or_create(
                level=level_obj,
                name=ability_name
            )

        # Добавляем известные заговоры (если их еще нет)
        SpecificColumnValue.objects.get_or_create(
            specific_column=known_cantrips,
            level=level_obj,
            defaults={"value": data["known_cantrips"]}
        )

        # Добавляем известные заклинания (если их еще нет)
        SpecificColumnValue.objects.get_or_create(
            specific_column=known_spells,
            level=level_obj,
            defaults={"value": data["known_spells"]}
        )

        # Добавляем ячейки заклинаний (если их еще нет)
        SpecificColumnValue.objects.get_or_create(
            specific_column=spell_slots,
            level=level_obj,
            defaults={"value": data["spell_slots"]}
        )


def reverse_populate_bard_data(apps, schema_editor):
    # Удаляем данные при откате миграции
    Class = apps.get_model('dnd', 'BaseClass')
    Level = apps.get_model('dnd', 'Level')
    SpecificColumn = apps.get_model('dnd', 'SpecificColumn')

    # Получаем объект "Бард"
    bard = Class.objects.filter(name="Бард").first()

    if bard:
        # Удаляем связанные уровни и специфические столбцы
        Level.objects.filter(class_obj=bard).delete()
        SpecificColumn.objects.filter(class_obj=bard).delete()


class Migration(migrations.Migration):
    dependencies = [
        ('dnd', '0002_auto_20230628_1047'),
    ]

    operations = [
        migrations.RunPython(populate_bard_data, reverse_populate_bard_data),
    ]

