import re
from django.db import migrations
import csv


# python manage.py makemigrations --empty dnd

def remove_brackets(text):
    cleaned_text = re.sub(r'\([^()]+\)', '', text)
    return cleaned_text.strip()


def combine_names(apps, schema_editor):
    Spell = apps.get_model('dnd', 'Spell')
    CharacterClass = apps.get_model('dnd', 'ClassChampion')
    CharacterClass = apps.get_model('dnd', 'ClassChampion')
    with open(
            'dnd/migrations/spells.csv',
            'r', newline='') as csvfile:
        reader = csv.reader(csvfile)

        for row in reader:
            class_actor = []
            class_ch = row[8].split(',')
            for i in class_ch:
                class_actor.append(i)

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
            for class_name in class_ch:
                class_name = remove_brackets(class_name)
                character_class, created = CharacterClass.objects.get_or_create(champion_class=class_name.strip())
                spell.class_actor.add(character_class)




class Migration(migrations.Migration):
    dependencies = [
        ('dnd', '0007_rename_subclasschampion_archetypechampion_and_more'),
    ]
    operations = [
        migrations.RunPython(combine_names),
    ]
