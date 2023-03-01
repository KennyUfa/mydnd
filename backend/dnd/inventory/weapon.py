class Weapon:
    type_usage = ''
    name = ''
    damage = ''
    damage_universal = ''
    price = ''
    damage_type = ''
    weight = ''
    properties = ''
    description = ''

    def info(self):
        return self.type_usage, self.name, self.damage, \
               self.damage_universal, self.price, self.damage_type, self.weight, \
               self.properties, self.description


class SimpleWeapon(Weapon):
    type_usage = "Простое рукопашное оружие"


class SimpleRangedWeapon(Weapon):
    type_usage = "Простое дальнобойное оружие"


class MilitaryRangedWeapons(Weapon):
    type_usage = "Воинское дальнобойное оружие"


class MilitaryHandToHandWeapon(Weapon):
    type_usage = "Воинское рукопашное оружие"

class BattleStaff(SimpleWeapon):
    name = "Боевой посох"
    damage = "1к6"
    damage_universal = '1к8'
    price = "2 cм."
    damage_type = "дробящий"
    weight = "4 фнт."
    properties = 'Универсальное (1к8)'


class Mace(SimpleWeapon):
    name = "Булава"
    damage = "1к6"
    price = "5 зм."
    damage_type = "дробящий"
    weight = "4 фнт."


class Club(SimpleWeapon):
    name = 'Дубинка'
    damage = '1к4'
    price = '1 см.'
    damage_type = 'дробящий'
    weight = '2 фнт.'
    properties = 'Лёгкое'


class Dagger(SimpleWeapon):
    name = 'Кинжал'
    damage = '1к4'
    price = '2 зм.'
    damage_type = 'колющий'
    weight = '1 фнт.'
    properties = 'Лёгкое, метательное (дис. 20/60), фехтовальное'


class Spear(SimpleWeapon):
    name = 'Копье'
    damage = '1к6'
    price = '1 зм.'
    damage_type = 'колющий'
    weight = '3 фнт.'
    properties = 'Метательное (дис. 20/60), универсальное (1к8)'
    damage_universal = '1к8'


class LightHammer(SimpleWeapon):
    name = 'Копье'
    damage = '1к4'
    price = '2 зм.'
    damage_type = 'дробящий'
    weight = '2 фнт.'
    properties = 'Лёгкое, метательное (дис. 20/60)'


class ThrowingSpear(SimpleWeapon):
    name = 'Метательное копье'
    damage = '1к6'
    price = '5 зм.'
    damage_type = 'колющий'
    weight = '2 фнт.'
    properties = 'Метательное (дис. 30/120)'


class Bat(SimpleWeapon):
    name = 'Копье'
    damage = '1к8'
    price = '2 cм.'
    damage_type = 'дробящий'
    weight = '10 фнт.'
    properties = 'Двуручное'


class HandAx(SimpleWeapon):
    name = 'Ручной топор'
    damage = '1к6'
    price = '5 зм.'
    damage_type = 'рубящий'
    weight = '2 фнт.'
    properties = 'Лёгкое, метательное (дис. 20/60)'


class Sickle(SimpleWeapon):
    name = 'Серп'
    damage = '1к4'
    price = '1 зм.'
    damage_type = 'рубящий'
    weight = '2 фнт.'
    properties = 'Лёгкое'


# _______________________________________________

class LightCrossbow(SimpleRangedWeapon):
    name = 'Арбалет, легкий'
    damage = '1к8'
    price = '25 зм.'
    damage_type = 'колющий'
    weight = '5 фнт.'
    properties = 'Боеприпас (дис. 80/320),двуручное, перезарядка'


class ShortBow(SimpleRangedWeapon):
    name = 'Короткий лук'
    damage = '1к6'
    price = '25 зм.'
    damage_type = 'колющий'
    weight = '2 фнт.'
    properties = 'Боеприпас (дис. 80/320),двуручное'


class Dart(SimpleRangedWeapon):
    name = 'Дротик'
    damage = '1к4'
    price = '5 мм.'
    damage_type = 'колющий'
    weight = '1/4 фнт.'
    properties = 'Метательное (дис. 20/60), фехтовальное'


class Sends(SimpleRangedWeapon):
    name = 'Праща'
    damage = '1к4'
    price = '1 см.'
    damage_type = 'дробящий'
    properties = 'Боеприпас (дис. 30/120)'


class Halberd(MilitaryHandToHandWeapon):
    name = 'Алебарда'
    damage = '1к10'
    price = '20 зм.'
    damage_type = 'рубящий'
    weight = '6 фнт.'
    properties = 'Двуручное, досягаемость, тяжёлое'


class WarPick(MilitaryHandToHandWeapon):
    name = 'Боевая кирка'
    damage = '1к8'
    price = '5 зм.'
    damage_type = 'колющий'
    weight = '2 фнт.'


class WarHammer(MilitaryHandToHandWeapon):
    name = 'Боевой молот'
    damage = '1к8'
    price = '15 зм.'
    damage_type = 'дробящий'
    weight = '2 фнт.'
    properties = 'Универсальное (1к10)'
    damage_universal = '1к10'


class BattleAx(MilitaryHandToHandWeapon):
    name = 'Боевой топор'
    damage = '1к8'
    price = '10 зм.'
    damage_type = 'рубящий'
    weight = '4 фнт.'
    properties = 'Универсальное (1к10)'
    damage_universal = '1к10'


class Glyph(MilitaryHandToHandWeapon):
    name = 'Глефа'
    damage = '1к10'
    price = '10 зм.'
    damage_type = 'рубящий'
    weight = '6 фнт.'
    properties = 'Двуручное, досягаемость, тяжёлое'


class TwoHandedSword(MilitaryHandToHandWeapon):
    name = 'Двуручный меч'
    damage = '2к6'
    price = '50 зм.'
    damage_type = 'рубящий'
    weight = '6 фнт.'
    properties = 'Двуручное, тяжёлое'


class LongSpear(MilitaryHandToHandWeapon):
    name = 'Длинное копье'
    damage = '1к12'
    price = '10 зм.'
    damage_type = 'колющий'
    weight = '6 фнт.'
    properties = 'Досягаемость, особое'


class LongSword(MilitaryHandToHandWeapon):
    name = 'Длинное копье'
    damage = '1к8'
    price = '15 зм.'
    damage_type = 'рубящий'
    weight = '3 фнт.'
    properties = 'Универсальное (1к10)'
    damage_universal = '1к10'


class Whip(MilitaryHandToHandWeapon):
    name = 'Кнут'
    damage = '1к4'
    price = '2 зм.'
    damage_type = 'рубящий'
    weight = '3 фнт.'
    properties = 'Досягаемость, фехтовальное'


class ShortSword(MilitaryHandToHandWeapon):
    name = 'Короткий меч'
    damage = '1к6'
    price = '10 зм.'
    damage_type = 'колющий'
    weight = '2 фнт.'
    properties = 'Лёгкое, фехтовальное'


class Hammer(MilitaryHandToHandWeapon):
    name = 'Молот'
    damage = '2к6'
    price = '10 зм.'
    damage_type = 'дробящий'
    weight = '10 фнт.'
    properties = 'Двуручное, тяжёлое'


class Morgenstern(MilitaryHandToHandWeapon):
    name = 'Моргенштерн'
    damage = '1к8'
    price = '15 зм.'
    damage_type = 'колющий'
    weight = '4 фнт.'


class Pika(MilitaryHandToHandWeapon):
    name = 'Пика'
    damage = '1к10'
    price = '5 зм.'
    damage_type = 'колющий'
    weight = '18 фнт.'
    properties = 'Двуручное, досягаемость, тяжёлое'


class Rapier(MilitaryHandToHandWeapon):
    name = 'Пика'
    damage = '1к8'
    price = '25 зм.'
    damage_type = 'колющий'
    weight = '2 фнт.'
    properties = 'Фехтовальное'


class Axe(MilitaryHandToHandWeapon):
    name = 'Пика'
    damage = '1к12'
    price = '30 зм.'
    damage_type = 'рубящий'
    weight = '7 фнт.'
    properties = 'Двуручное, тяжёлое'


class Scimitar(MilitaryHandToHandWeapon):
    name = 'Скимитар'
    damage = '1к6'
    price = '25 зм.'
    damage_type = 'рубящий'
    weight = '3 фнт.'
    properties = 'Лёгкое, фехтовальное'


class Trident(MilitaryHandToHandWeapon):
    name = 'Трезубец'
    damage = '1к6'
    price = '5 зм.'
    damage_type = 'колющий'
    weight = '4 фнт.'
    properties = 'Метательное (дис. 20/60), Универсальное (1к8)'
    damage_universal = '1к8'


class Cep(MilitaryHandToHandWeapon):
    name = 'Цеп'
    damage = '1к8'
    price = '10 зм.'
    damage_type = 'дробящий'
    weight = '2 фнт.'


class CrossbowManual(MilitaryRangedWeapons):
    name = 'Арбалет, ручной'
    damage = '1к6'
    price = '75 зм.'
    damage_type = 'колющий'
    weight = '3 фнт.'
    properties = 'Боеприпас (дис. 30/120), легкое, перезарядка'


class CrossbowHeavy(MilitaryRangedWeapons):
    name = 'Арбалет, тяжелый'
    damage = '1к10'
    price = '50 зм.'
    damage_type = 'колющий'
    weight = '18 фнт.'
    properties = 'Боеприпас (дис. 100/400), двуручное, перезарядка, тяжёлое'


class LongBow(MilitaryRangedWeapons):
    name = 'Длинный лук'
    damage = '1к8'
    price = '50 зм.'
    damage_type = 'колющий'
    weight = '2 фнт.'
    properties = 'Боеприпас (дис. 150/600), двуручное, тяжёлое'


class BlowPipe(MilitaryRangedWeapons):
    name = 'Духовая трубка'
    damage = '1к8'
    price = '10 зм.'
    damage_type = 'колющий'
    weight = '1 фнт.'
    properties = 'Боеприпас (дис. 25/100), перезарядка'


class Net(MilitaryRangedWeapons):
    name = 'Сеть'
    price = '1 зм.'
    weight = '3 фнт.'
    properties = 'Метательное (дис. 5/15), особое'


weapons = [BattleStaff, Mace, LightCrossbow, ShortBow]
