# Generated by Django 4.1.3 on 2023-06-29 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dnd', '0003_classchampion_possession_bonus'),
    ]

    operations = [
        migrations.AddField(
            model_name='classchampion',
            name='available_gear',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='classchampion',
            name='dice_hit',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='classchampion',
            name='hit_first_level',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='classchampion',
            name='hit_next_level',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='classchampion',
            name='protect_dice',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='classchampion',
            name='skill_check',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
