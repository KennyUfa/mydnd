# Generated by Django 5.1.4 on 2025-01-21 17:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dnd', '0026_rename_protect_char_state_character_protect_state_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='character',
            old_name='origin',
            new_name='my_origin',
        ),
    ]
