import json

import bs4
from django.db import migrations


def eqvipmentsdb(apps, s):
    db_weapon = apps.get_model('dnd', 'Equipment')
    db_weapon_type = apps.get_model('dnd', 'SubType')
    db_item = apps.get_model('dnd', 'Item')
    db_ItemType = apps.get_model('dnd', 'TypeItem')
    db_ItemRarity = apps.get_model('dnd', 'Rarity')

    with open('dnd/migrations/Equipment.json', 'r', encoding='utf-8') as \
            equipment_json:
        for eq in equipment_json:
            eq_info = bs4.BeautifulSoup(eq, features="html.parser").text
            info = json.loads(eq_info)
            if 'Оружие' in info['categories']:
                continue
            if 'Доспех' in info['categories']:
                continue
            else:
                x = None
                try:
                    info['categories'].remove('Cнаряжение')
                except Exception:
                    pass
                try:
                    print(info['categories'])
                    x = db_weapon_type.objects.create(info['categories'][0])
                except Exception:
                    continue
                db_ItemType.objects.get_or_create(
                    description='Снаряжение')
                db_ItemRarity.objects.get_or_create(
                    description='Обычная')
                db_item.objects.create(name=info['name']['rus'],
                                      type=db_ItemType.objects.get(
                                          description='Снаряжение'),
                                      rarity=db_ItemRarity.objects.get(
                                          description='Обычная'))


class Migration(migrations.Migration):
    operations = [migrations.RunPython(eqvipmentsdb),
                  ]

    dependencies = [
        ('dnd', '0001_initial'),
    ]

