# Generated by Django 5.1.4 on 2025-01-26 14:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dnd', '0011_customfeature_customorigin'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CustomFeature',
            new_name='CustomRaceFeature',
        ),
    ]