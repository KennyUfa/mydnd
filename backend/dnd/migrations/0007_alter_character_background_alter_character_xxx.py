# Generated by Django 4.1.3 on 2023-01-19 10:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dnd', '0006_alter_character_background_alter_character_xxx'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='background',
            field=models.ForeignKey(default=25, on_delete=django.db.models.deletion.CASCADE, to='dnd.backgroundmodel'),
        ),
        migrations.AlterField(
            model_name='character',
            name='xxx',
            field=models.ForeignKey(default=11, on_delete=django.db.models.deletion.CASCADE, to='dnd.strengthdmodel'),
        ),
    ]