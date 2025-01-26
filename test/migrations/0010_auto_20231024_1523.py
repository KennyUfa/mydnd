import re
import time

from django.db import migrations
import csv


# python manage.py makemigrations --empty dnd

def remove_brackets(text):
    cleaned_text = re.sub(r'\([^()]+\)', '', text)
    return cleaned_text.strip()


def extract_contents(text):
    pattern = r'\(([^()]+)\)'
    matches = re.findall(pattern, text)
    t = matches[0]

    for match in matches:
        text = text.replace(f'({match})', '')
    return text.strip(), t


def combine_names(apps, schema_editor):
    Spell = apps.get_model('dnd', 'Spell')
    CharacterClass = apps.get_model('dnd', 'ClassChampion')
    ArchetypeChampion = apps.get_model('dnd', 'Archetype')

    with open(
            'dnd/migrations/spells.csv',
            'r', newline='') as csvfile:
        reader = csv.reader(csvfile)

        for row in reader:

            class_ch = row[8].split(',')
            arh = row[9].split(',')

            spell = Spell.objects.create(link=row[0],
                                         name=row[1],
                                         lvl=row[2],
                                         school=row[3],
                                         time_cast=row[4],
                                         distance=row[5],
                                         components=row[6],
                                         timing=row[7],
                                         # class_actor=row[8],
                                         # architype=row[9],
                                         origin=row[10],
                                         instruction=row[11],
                                         )

            # создает связь заклинаний с классами
            print(row[1])
            if class_ch[0] == '':
                # print('11111pass')
                continue

            else:
                # print('11111')
                # print(class_ch)
                for class_name in class_ch:
                    class_name = remove_brackets(class_name)
                    print(class_name)
                    character_class, created = CharacterClass.objects.get_or_create(champion_class=class_name.strip())
                    spell.class_actor.add(character_class)

            if arh[0] == '':
                # print('222222pass')
                continue
            else:
                # print('22222')
                # print(arh)
                for i in arh:
                    text_before, contents = extract_contents(i.strip())
                    # print(text_before, contents)
                    character_class, created = CharacterClass.objects.get_or_create(champion_class=contents.strip())
                    subclass_name = text_before
                    # print(text_before + '--' + contents)
                    print(character_class)
                    archetype, created = ArchetypeChampion.objects.get_or_create(
                        character_class=CharacterClass.objects.get(champion_class=contents.strip()),
                        name=subclass_name
                    )
                    spell.archetype.add(archetype)


class Migration(migrations.Migration):
    dependencies = [
        ('dnd', '0009_remove_archetype_additional_spells_spell_archetype'),
    ]

    operations = [
        migrations.RunPython(combine_names),
    ]
