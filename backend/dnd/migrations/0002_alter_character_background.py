# Generated by Django 4.1.3 on 2023-01-19 09:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dnd', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='background',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='dnd.backgroundmodel'),
        ),
    ]