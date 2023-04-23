import json

import bs4
from django.db import migrations, transaction


def weapondb(apps, schema_editor):
    db_weapon = apps.get_model('dnd', 'Weapon')
    db_weapon_type = apps.get_model('dnd', 'SubType')
    db_weapon_properties = apps.get_model('dnd', 'Properties')
    db_item = apps.get_model('dnd', 'Item')
    db_ItemType = apps.get_model('dnd', 'TypeItem')
    db_ItemRarity = apps.get_model('dnd', 'Rarity')

    with open('dnd/migrations/weapon.json', 'r', encoding='utf-8') as \
            weapons_json:
        for w in weapons_json:
            w_info = bs4.BeautifulSoup(w, features="html.parser").text
            weapon_info = json.loads(w_info)
            db_weapon_type.objects.get_or_create(
                description=weapon_info['type']['name'])
            db_ItemType.objects.get_or_create(description='Оружие')
            db_ItemRarity.objects.get_or_create(description='Обычная')
            item = db_item.objects.create(name=weapon_info['name']['rus'],
                                          type=db_ItemType.objects.get(
                                              description='Оружие'),
                                          rarity=db_ItemRarity.objects.get(
                                              description='Обычная'))

            try:
                hb = weapon_info['homebrew']
            except Exception:
                hb = False

            prop = []
            for i in weapon_info['properties']:
                if 'distance' in i:
                    prop.append(i['name'] + ' ' + i['distance'])
                else:
                    prop.append(i['name'])

            weapon = db_weapon.objects.create(
                item=item,
                homebrew=True if hb else False,
                type=db_weapon_type.objects.get(
                    description=weapon_info['type']['name']),
                damage='-' if 'dice' not in weapon_info['damage'] else
                weapon_info['damage']['dice'],
                damage_type='без урона' if 'dice' not in weapon_info['damage']
                else
                weapon_info['damage']['type'],
                price=weapon_info['price'],
                weight=weapon_info['weight'],
                source=weapon_info['source']['name'],
                description='-' if 'description' not in weapon_info else
                weapon_info['description'],
                special='-' if 'special' not in weapon_info else
                weapon_info['special'],
            )
            weapon.save()
            temp = ''
            if not prop:
                pass
            else:
                for i in prop:
                    if not db_weapon_properties.objects.filter(
                            name=i):
                        with transaction.atomic():
                            temp = db_weapon_properties(name=i)
                            temp.save()
                            weapon.properties.add(temp)
                    else:
                        with transaction.atomic():
                            temp = db_weapon_properties.objects.filter(
                                name=i.strip())[0]
                            weapon.properties.add(temp)


class Migration(migrations.Migration):
    operations = [migrations.RunPython(weapondb),
                  ]

    dependencies = [
        ('dnd', '0008_auto_20230421_1348'),
    ]
