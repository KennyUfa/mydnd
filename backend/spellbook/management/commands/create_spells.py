import csv

from django.core.management import BaseCommand

from champion_class.models import BaseClass, Archetype
from spellbook.models import MagicSchool, Spell


def clean_class_name(class_name):
    """
    Удаляет всё, что находится в скобках, и лишние пробелы.
    Пример: "бард (Tasha's Cauldron of Everything)" -> "бард"
    """
    return class_name.split(' (')[0].strip()



class Command(BaseCommand):
    help = 'Добавление заклинаний'

    def handle(self, *args, **options):
        with open('spellbook/management/commands/spells.csv', 'r', newline='', encoding="UTF-8") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if row[2] == "Заговор" or row[2] == "заговор":
                    level = 0
                else:
                    level = int(row[2][0])
                try:
                    school_choice, _ = MagicSchool.objects.get_or_create(name=row[3].split()[0])

                    spell,_ = Spell.objects.get_or_create(
                        link=row[0],
                        name=row[1],
                        level=level,
                        school=school_choice,
                        time_cast=row[4],
                        distance=row[5],
                        components=row[6],
                        timing=row[7],
                        origin=row[10],
                        instruction=row[11],
                    )
                    # Обрабатываем class_actor (ManyToManyField)
                    class_actors = []
                    for actor_name in row[8].split(', '):  # Предположим, что row[8] содержит строку "колдун, бард, волшебник"
                        if actor_name.strip():  # Проверяем, что строка не пустая
                            cleaned_name = clean_class_name(actor_name)  # Очищаем имя
                            actor, created = BaseClass.objects.get_or_create(name=cleaned_name)
                            class_actors.append(actor)

                    spell.class_actor.set(class_actors)

                    archetypes = []
                    for archetype_name in row[9].split(', '):  # Предположим, что row[9] содержит строку "клятвопреступник (паладин)"
                        if archetype_name.strip():  # Проверяем, что строка не пустая
                            # Извлекаем название архетипа и класс
                            archetype_name_clean = archetype_name.split(' (')[0].strip()  # "клятвопреступник"
                            class_name = archetype_name.split(' (')[1].replace(')', '').strip()  # "паладин"

                            # Очищаем имя класса
                            cleaned_class_name = clean_class_name(class_name)

                            # Получаем или создаем объект BaseClass
                            character_class, _ = BaseClass.objects.get_or_create(name=cleaned_class_name)

                            # Получаем или создаем объект Archetype
                            archetype, _ = Archetype.objects.get_or_create(
                                name=archetype_name_clean,
                                character_class=character_class
                            )
                            archetypes.append(archetype)

                    spell.archetype.set(archetypes)




                except Exception as e:
                        print(f"Ошибка при создании заклинания {row[1]}: {e}")
                        break
