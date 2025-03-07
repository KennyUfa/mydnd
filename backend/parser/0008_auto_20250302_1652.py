from django.db import migrations


def add_fighter_data(apps, schema_editor):
    BaseClass = apps.get_model('dnd', 'BaseClass')
    Level = apps.get_model('dnd', 'Level')
    Ability = apps.get_model('dnd', 'Ability')

    # Создаем базовый класс "Воин"
    fighter_class, _ = BaseClass.objects.get_or_create(
        name__iexact="воин",  # Ищем без учета регистра
        defaults={
            "name": "Воин",
            "description": "Мастер ближнего боя, выносливый защитник.",
            "hit_dice": "d10",
            "hit_at_first_level": "10 + модификатор телосложения",
            "hit_at_next_level": "6 + модификатор телосложения",
            "possession_armor": "Все доспехи",
            "possession_weapon": "Простое и военное оружие",
            "possession_instrument": "Нет",
            "saving_throws": "Сила, Телосложение"
        }
    )

    # Список способностей для каждого уровня
    fighter_abilities_by_level = {
        1: [
            ("Боевой стиль", "Выбор стиля боя."),
            ("Второе дыхание", "Используете бонусное действие для восстановления хитов."),
        ],
        2: [
            ("Атака с напряжением", "Делаете дополнительную атаку."),
        ],
        3: [
            ("Путь боевого мастера", "Выбор пути боевого мастера."),
        ],
        7: [
            ("Неутомимость", "Устойчивость к эффектам истощения."),
        ],
        10: [
            ("Дополнительный боевой стиль", "Выбор второго боевого стиля."),
        ],
        15: [
            ("Стойкость перед смертью", "Устойчивость к эффектам урона."),
        ],
        18: [
            ("Улучшенная атака с напряжением", "Делаете еще одну дополнительную атаку."),
        ],
        20: [
            ("Выживший", "Получаете 4 дополнительных хита при каждом отдыхе."),
        ],
    }

    # Создаем уровни для воина
    for lvl in range(1, 21):
        level, _ = Level.objects.get_or_create(
            class_obj=fighter_class,  # Передаем объект fighter_class
            level=lvl,
            defaults={"proficiency_bonus": (lvl // 4) + 2}
        )

        # Добавляем способности для текущего уровня
        if lvl in fighter_abilities_by_level:
            for ability_name, ability_description in fighter_abilities_by_level[lvl]:
                Ability.objects.get_or_create(
                    level=level,
                    name=ability_name,
                    defaults={"description": ability_description}
                )


class Migration(migrations.Migration):

    dependencies = [
        ('dnd', '0002_auto_20230628_1047'),
    ]

    operations = [
        migrations.RunPython(add_fighter_data),
    ]