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
