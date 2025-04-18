# Generated by Django 5.1.4 on 2025-04-09 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dnd', '0008_auto_20250409_0517'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='inventoryitem',
            options={'ordering': ['-put_on'], 'verbose_name': 'предмет', 'verbose_name_plural': 'инвентарь'},
        ),
        migrations.AlterField(
            model_name='race',
            name='background',
            field=models.ManyToManyField(blank=True, related_name='race', to='dnd.racebackground', verbose_name='История расы'),
        ),
    ]
