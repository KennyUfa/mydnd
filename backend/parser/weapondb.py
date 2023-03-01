# Generated by Django 4.1.3 on 2023-02-28 14:31

from django.db import migrations, transaction
from dnd.inventory import weapon
import inspect


def combine_names(apps, schema_editor):
    db_weapon = apps.get_model('dnd', 'Weapon')
    db_weapon_type = apps.get_model('dnd', 'WeaponType')
    db_weapon_properties = apps.get_model('dnd', 'Properties')
    for name, obj in inspect.getmembers(weapon):
        if inspect.isclass(obj):
            if obj.__name__ in ('SimpleRangedWeapon', 'SimpleWeapon',
                                'MilitaryHandToHandWeapon',
                                'MilitaryRangedWeapons','Weapon'):
                pass
            else:
                wep = obj()
                print(wep.info())

                db_weapon_type.objects.get_or_create(description=wep.info()[0])

                x = db_weapon.objects.create(
                    type_id=db_weapon_type.objects.get(
                        description=wep.info()[0]).id,
                    name=wep.info()[1],
                    damage=wep.info()[2],
                    damage_universal=wep.info()[3],
                    price=wep.info()[4],
                    damage_type=wep.info()[5],
                    weight=wep.info()[6],
                    # properties =db_weapon_properties.objects.add(
                    #     name=wep.info()[7]).id,
                    description=wep.info()[8],
                )
                x.save()
                temp = ''
                if wep.info()[7] == '':
                    pass
                else:
                    for i in wep.info()[7].split(','):
                        if not db_weapon_properties.objects.filter(
                                name=i.strip()):
                            with transaction.atomic():
                                temp = db_weapon_properties(name=i.strip())
                                temp.save()
                                x.properties.add(temp)
                        else:
                            with transaction.atomic():
                                temp = db_weapon_properties.objects.filter(
                                    name=i.strip())[0]
                                x.properties.add(temp)


class Migration(migrations.Migration):

    dependencies = [
        ('dnd', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(combine_names),
    ]
