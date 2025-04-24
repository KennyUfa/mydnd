from django.core.management import BaseCommand
import json
import bs4
from django.db import transaction

from item.models import SubType, TypeItem, Rarity, Item, Armor, Equipment, Properties, Weapon, MagicItems


class Command(BaseCommand):
    help = 'Добавление заклинаний'

    def handle(self, *args, **options):
        with open('item/management/commands/armore.json', 'r', encoding='utf-8') as \
                weapons_json:
            for w in weapons_json:
                w_info = bs4.BeautifulSoup(w, features="html.parser").text
                info = json.loads(w_info)
                SubType.objects.get_or_create(
                    description=info['type']['name'])
                TypeItem.objects.get_or_create(description='Доспехи')
                Rarity.objects.get_or_create(description='Обычный')
                item = Item.objects.create(name=info['name']['rus'],
                                              type=TypeItem.objects.get(
                                                  description='Доспехи'),
                                              rarity=Rarity.objects.get(
                                                  description='Обычный'))
                if 'homebrew' in info:
                    # TODO пока без хоумбрю
                    pass
                else:
                    armor = Armor.objects.create(
                        item=item,
                        sub_type=SubType.objects.get(
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

        with open('item/management/commands/Equipment.json', 'r', encoding='utf-8') as \
                equipment_json:
            for eq in equipment_json:
                eq_info = bs4.BeautifulSoup(eq, features="html.parser").text
                info = json.loads(eq_info)
                if 'Оружие' in info['categories']:
                    continue
                if 'Доспех' in info['categories']:
                    continue
                else:
                    if 'homebrew' in info:
                        pass
                    else:
                        x = None
                        try:
                            info['categories'].remove('Cнаряжение')
                        except Exception:
                            pass
                        try:
                            x = SubType.objects.create(info['categories'][0])
                        except Exception:
                            pass

                        TypeItem.objects.get_or_create(
                            description='Снаряжение')
                        Rarity.objects.get_or_create(
                            description='Обычный')
                        item = Item.objects.create(name=info['name']['rus'],
                                                      type=TypeItem.objects.get(
                                                          description='Снаряжение'),
                                                      rarity=Rarity.objects.get(
                                                          description='Обычный'))
                        equipment = Equipment.objects.create(
                            item=item,
                            homebrew=True if 'homebrew' in info else False,
                            price=info['price'] if 'price' in info else '-',
                            weight=info['weight'] if 'weight' in info else '-',
                            source=info['source']['name'],
                            description='-' if 'description' not in info else
                            info['description'],
                        )
                        if x:
                            print(x)
                            equipment.sub_type = x

                        equipment.save()

        with open('item/management/commands/weapon.json', 'r', encoding='utf-8') as \
                weapons_json:
            for w in weapons_json:
                w_info = bs4.BeautifulSoup(w, features="html.parser").text
                weapon_info = json.loads(w_info)
                if 'homebrew' in weapon_info:
                    pass
                else:
                    SubType.objects.get_or_create(
                        description=weapon_info['type']['name'])
                    TypeItem.objects.get_or_create(description='Оружие')
                    Rarity.objects.get_or_create(description='Обычный')
                    item = Item.objects.create(name=weapon_info['name']['rus'],
                                                  type=TypeItem.objects.get(
                                                      description='Оружие'),
                                                  rarity=Rarity.objects.get(
                                                      description='Обычный'))

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

                    weapon = Weapon.objects.create(
                        item=item,
                        homebrew=True if hb else False,
                        type=SubType.objects.get(
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
                            if not Properties.objects.filter(
                                    name=i):
                                with transaction.atomic():
                                    temp = Properties(name=i)
                                    temp.save()
                                    weapon.properties.add(temp)
                            else:
                                with transaction.atomic():
                                    temp = Properties.objects.filter(
                                        name=i.strip()).first()
                                    weapon.properties.add(temp)

        with open('item/management/commands/magik_eq.json', 'r', encoding='utf-8') as \
                item_json:
            for w in item_json:
                w_info = bs4.BeautifulSoup(w, features="html.parser").text
                info = json.loads(w_info)
                if 'homebrew' in info:
                    pass
                else:
                    a = info['name']['rus']
                    b = 'Магические предметы'
                    c = info['rarity']['name']

                    if c in ['обычная', 'обычный', 'обычное']:
                        c = 'Обычный'
                    elif c in ['необычное', 'необычная', 'необычный']:
                        c = 'Необычный'
                    elif c in ['редкий', 'редкое', 'редкая']:
                        c = 'Редкий'
                    elif c in ['очень редкое', 'очень редкая', 'очень редкий']:
                        c = 'Очень редкий'
                    elif c in ['легендарный', 'легендарное', 'легендарный']:
                        c = 'Легендарный'
                    elif c in ['редкость варьируется']:
                        c = 'Редкость варьируется'
                    elif c in ['редкость не определена']:
                        c = 'Редкость не определена'
                    elif c in ['артефакт']:
                        c = 'Артефакт'

                    f = '-'
                    if 'detailCustamization' in info:
                        for i in info['detailCustamization']:
                            f += i + ', '
                    SubType.objects.get_or_create(
                        description=info['type']['name'])
                    TypeItem.objects.get_or_create(description=b)
                    Rarity.objects.get_or_create(description=c)
                    item = Item.objects.create(name=a,
                                                  type=TypeItem.objects.get(
                                                      description=b),
                                                  rarity=Rarity.objects.get(
                                                      description=c))

                    item_m = MagicItems.objects.create(
                        item=item,
                        sub_type=SubType.objects.get(
                            description=info['type']['name']),
                        homebrew=True if 'homebrew' in info else False,
                        price=info['cost']['dmg'] + ', или ' + info['cost']['xge'] if
                        'cost' in info else '-',
                        source=info['source']['name'],
                        description=info['description'].replace('\xa0', ' '),
                        customization=True if 'customization' in info else False,
                        detailCustamization=f,
                        detailType=['detailType'] if 'detailType' in info else '',
                    )
                    item_m.save()