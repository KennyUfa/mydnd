import json

import bs4
from django.db import migrations


def armordb(apps, schema_editor):
    db_weapon = apps.get_model('dnd', 'Armor')
    db_weapon_type = apps.get_model('dnd', 'SubType')
    db_item = apps.get_model('dnd', 'Item')
    db_ItemType = apps.get_model('dnd', 'TypeItem')
    db_ItemRarity = apps.get_model('dnd', 'Rarity')

    with open('dnd/migrations/armore.json', 'r', encoding='utf-8') as \
            weapons_json:
        for w in weapons_json:
            w_info = bs4.BeautifulSoup(w, features="html.parser").text
            info = json.loads(w_info)
            db_weapon_type.objects.get_or_create(
                description=info['type']['name'])
            db_ItemType.objects.get_or_create(description='Доспехи')
            db_ItemRarity.objects.get_or_create(description='Обычная')
            item = db_item.objects.create(name=info['name']['rus'],
                                          type=db_ItemType.objects.get(
                                              description='Доспехи'),
                                          rarity=db_ItemRarity.objects.get(
                                              description='Обычная'))

            armor = db_weapon.objects.create(
                item=item,
                sub_type=db_weapon_type.objects.get(
                    description=info['type']['name']),
                homebrew=True if 'homebrew' in info else False,
                price=info['price'],
                weight=info['weight'],
                source=info['source']['name'],
                armore=info['armorClass'],
                duration=info['duration'],

                disadvantage=False if 'disadvantage' not in info else
                True,
                description=info['description'],
                requirement=info['requirement'] if 'requirement' in info
                else '-',
            )
            armor.save()


class Migration(migrations.Migration):
    operations = [migrations.RunPython(armordb),
                  ]

    dependencies = [
        ('dnd', '0009_auto_20230421_1408'),
    ]
