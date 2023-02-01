# Generated by Django 4.1.3 on 2023-01-31 04:51
from django.db import migrations
import csv


def combine_names(apps, schema_editor):
    x = 0
    # We can't import the Person model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    Spell = apps.get_model('dnd', 'DndSpell')
    with open('dnd/spells.csv', 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            print(row[1])
            Spell.objects.create(link=row[0],
                                 name=row[1],
                                 lvl=row[2],
                                 school=row[3],
                                 time_cast=row[4],
                                 distance=row[5],
                                 components=row[6],
                                 timing=row[7],
                                 class_actor=row[8],
                                 architype=row[9],
                                 origin=row[10],
                                 instruction=row[11],
                                 )


class Migration(migrations.Migration):
    dependencies = [
        ('dnd', '0012_protectstatemodel_skillstatemodel_and_more'),
    ]

    operations = [
        migrations.RunPython(combine_names),
    ]
