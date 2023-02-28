# Generated by Django 4.1.3 on 2023-02-27 14:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dnd', '0002_auto_20230223_0654'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shield',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='dnd.weapontype')),
            ],
        ),
    ]
