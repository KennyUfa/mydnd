from django.db import migrations
import csv
import json

import bs4
from django.db import migrations, transaction

from dnd.models import Archetype, BaseClass


# python manage.py makemigrations --empty dnd

def clean_class_name(class_name):
    """
    Удаляет всё, что находится в скобках, и лишние пробелы.
    Пример: "бард (Tasha's Cauldron of Everything)" -> "бард"
    """
    return class_name.split(' (')[0].strip()

def combine_names(apps, schema_editor):
    Spell = apps.get_model('dnd', 'Spell')
    BaseClass = apps.get_model('dnd', 'BaseClass')
    Archetype = apps.get_model('dnd', 'Archetype')

    with open('dnd/migrations/spells.csv', 'r', newline='', encoding="UTF-8") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            print(row[1])
            try:
                with transaction.atomic():
                    # Создаем объект Spell
                    spell = Spell.objects.create(
                        link=row[0],
                        name=row[1],
                        lvl=row[2],
                        school=row[3],
                        time_cast=row[4],
                        distance=row[5],
                        components=row[6],
                        timing=row[7],
                        origin=row[10],
                        instruction=row[11],
                    )

                    # Обрабатываем class_actor (ManyToManyField)
                    class_actors = []
                    for actor_name in row[8].split(', '):  # Предположим, что row[8] содержит строку "колдун, бард, волшебник"
                        if actor_name.strip():  # Проверяем, что строка не пустая
                            cleaned_name = clean_class_name(actor_name)  # Очищаем имя
                            actor, created = BaseClass.objects.get_or_create(name=cleaned_name)
                            class_actors.append(actor)

                    spell.class_actor.set(class_actors)  # Используем метод .set() с объектами

                    # Обрабатываем archetype (ManyToManyField)
                    archetypes = []
                    for archetype_name in row[9].split(', '):  # Предположим, что row[9] содержит строку "клятвопреступник (паладин)"
                        if archetype_name.strip():  # Проверяем, что строка не пустая
                            # Извлекаем название архетипа и класс
                            archetype_name_clean = archetype_name.split(' (')[0].strip()  # "клятвопреступник"
                            class_name = archetype_name.split(' (')[1].replace(')', '').strip()  # "паладин"

                            # Очищаем имя класса
                            cleaned_class_name = clean_class_name(class_name)

                            # Получаем или создаем объект BaseClass
                            character_class, _ = BaseClass.objects.get_or_create(name=cleaned_class_name)

                            # Получаем или создаем объект Archetype
                            archetype, _ = Archetype.objects.get_or_create(
                                name=archetype_name_clean,
                                character_class=character_class
                            )
                            archetypes.append(archetype)

                    spell.archetype.set(archetypes)  # Используем метод .set() с объектами

            except Exception as e:
                print(f"Ошибка при создании заклинания {row[1]}: {e}")
                break

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
                    x = db_weapon_type.objects.create(info['categories'][0])
                except Exception:
                    pass

                db_ItemType.objects.get_or_create(
                    description='Снаряжение')
                db_ItemRarity.objects.get_or_create(
                    description='Обычная')
                item = db_item.objects.create(name=info['name']['rus'],
                                              type=db_ItemType.objects.get(
                                                  description='Снаряжение'),
                                              rarity=db_ItemRarity.objects.get(
                                                  description='Обычная'))
                equipment = db_weapon.objects.create(
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
    dependencies = [
        ('dnd', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(combine_names),
        migrations.RunPython(armordb),
        migrations.RunPython(eqvipmentsdb),
        migrations.RunPython(weapondb),
        migrations.RunPython(magicdb),

    ]
