# Generated by Django 5.1.4 on 2025-01-21 10:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dnd', '0021_remove_spellslotprogression_slots_level_0_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='spellslotprogression',
            name='class_obj',
        ),
        migrations.RemoveField(
            model_name='subclass',
            name='parent_class',
        ),
        migrations.AlterModelOptions(
            name='baseclass',
            options={},
        ),
        migrations.RemoveField(
            model_name='baseclass',
            name='has_spell_slots',
        ),
        migrations.RemoveField(
            model_name='baseclass',
            name='hit_dice',
        ),
        migrations.RemoveField(
            model_name='baseclass',
            name='primary_abilities',
        ),
        migrations.RemoveField(
            model_name='baseclass',
            name='proficiencies',
        ),
        migrations.RemoveField(
            model_name='baseclass',
            name='saving_throws',
        ),
        migrations.RemoveField(
            model_name='baseclass',
            name='skill_options',
        ),
        migrations.AddField(
            model_name='baseclass',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Описание класса'),
        ),
        migrations.AlterField(
            model_name='baseclass',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Название класса'),
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.PositiveIntegerField(verbose_name='Уровень')),
                ('proficiency_bonus', models.PositiveIntegerField(verbose_name='Бонус мастерства')),
                ('class_obj', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='levels', to='dnd.baseclass', verbose_name='Класс')),
            ],
            options={
                'ordering': ['class_obj', 'level'],
                'unique_together': {('class_obj', 'level')},
            },
        ),
        migrations.CreateModel(
            name='Ability',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название способности')),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='abilities', to='dnd.level', verbose_name='Уровень')),
            ],
        ),
        migrations.CreateModel(
            name='SpecificColumn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название специфического столбца')),
                ('class_obj', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='specific_columns', to='dnd.baseclass', verbose_name='Класс')),
            ],
        ),
        migrations.CreateModel(
            name='SpecificColumnValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.JSONField(verbose_name='Значение')),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='specific_column_values', to='dnd.level', verbose_name='Уровень')),
                ('specific_column', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='values', to='dnd.specificcolumn', verbose_name='Специфический столбец')),
            ],
            options={
                'unique_together': {('specific_column', 'level')},
            },
        ),
        migrations.DeleteModel(
            name='ClassFeature',
        ),
        migrations.DeleteModel(
            name='SpellSlotProgression',
        ),
        migrations.DeleteModel(
            name='Subclass',
        ),
    ]
