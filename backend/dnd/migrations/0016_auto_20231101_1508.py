# Generated by Django 4.1.3 on 2023-11-01 15:08

from django.db import migrations
from parser.mir import mir


def combine_names(apps,a):
    world_outlook = apps.get_model('dnd', 'WorldOutlook')
    for i, k in mir.items():
        world_outlook.objects.create(name=i, description=k)


class Migration(migrations.Migration):
    dependencies = [
        ('dnd', '0015_rename_world_outlook_worldoutlook_name_and_more'),
    ]

    operations = [
        migrations.RunPython(combine_names),
    ]