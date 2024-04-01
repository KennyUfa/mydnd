# Generated by Django 4.1.3 on 2023-10-23 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dnd', '0006_subclasschampion_main_class'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SubclassChampion',
            new_name='ArchetypeChampion',
        ),
        migrations.RemoveField(
            model_name='classchampion',
            name='additional_spell',
        ),
        migrations.RemoveField(
            model_name='spell',
            name='architype',
        ),
        migrations.AddField(
            model_name='spell',
            name='archetype',
            field=models.ManyToManyField(blank=True, related_name='archetype_spells', to='dnd.archetypechampion'),
        ),
        migrations.RemoveField(
            model_name='spell',
            name='class_actor',
        ),
        migrations.AddField(
            model_name='spell',
            name='class_actor',
            field=models.ManyToManyField(blank=True, related_name='class_spells', to='dnd.classchampion'),
        ),
    ]
