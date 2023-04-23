import json

import bs4
from django.db import migrations


def magicdb(apps, schema_editor):
    db_weapon = apps.get_model('dnd', 'MagicItems')
    db_item = apps.get_model('dnd', 'Item')
    db_ItemType = apps.get_model('dnd', 'TypeItem')
    db_ItemRarity = apps.get_model('dnd', 'Rarity')
    db_weapon_type = apps.get_model('dnd', 'SubType')

    with open('dnd/migrations/magik_eq.json', 'r', encoding='utf-8') as \
            item_json:
        for w in item_json:
            w_info = bs4.BeautifulSoup(w, features="html.parser").text
            info = json.loads(w_info)
            a = info['name']['rus']
            b = 'Магические предметы'
            c = info['rarity']['name']
            f = '-'
            if 'detailCustamization' in info:
                for i in info['detailCustamization']:
                    f += i + ', '
            db_weapon_type.objects.get_or_create(
                description=info['type']['name'])
            db_ItemType.objects.get_or_create(description=b)
            db_ItemRarity.objects.get_or_create(description=c)
            item = db_item.objects.create(name=a,
                                          type=db_ItemType.objects.get(
                                              description=b),
                                          rarity=db_ItemRarity.objects.get(
                                              description=c))

            item_m = db_weapon.objects.create(
                item=item,
                sub_type=db_weapon_type.objects.get(
                    description=info['type']['name']),
                homebrew=True if 'homebrew' in info else False,
                price=info['cost']['dmg']+', или '+ info['cost']['xge'] if
                       'cost' in info else '-',
                source=info['source']['name'],
                description=info['description'].replace('\xa0',' '),
                customization=True if 'customization' in info else False,
                detailCustamization=f,
                detailType=['detailType'] if 'detailType' in info else '',
            )
            item_m.save()


class Migration(migrations.Migration):
    operations = [migrations.RunPython(magicdb),
                  ]

    dependencies = [
        ('dnd', '0011_magicitems_remove_ring_item_remove_scroll_item_and_more'),
    ]

