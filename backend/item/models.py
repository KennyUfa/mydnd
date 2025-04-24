# Общий инвентарь
from django.db import models
from character.models import Character


class Properties(models.Model):
    name = models.CharField(blank=True, null=True, max_length=200, default='')
    description = models.CharField(blank=True, null=True, max_length=2000,
                                   default='')

    def __str__(self):
        return self.name


class TypeItem(models.Model):
    description = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.description


class Rarity(models.Model):
    description = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"{self.description}-{self.id}"


class Item(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True, )
    type = models.ForeignKey(TypeItem, on_delete=models.CASCADE, blank=True)
    rarity = models.ForeignKey(Rarity, on_delete=models.CASCADE, blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


# Оружие
class SubType(models.Model):
    description = models.CharField(blank=True, null=True, max_length=200)

    def __str__(self):
        return self.description


class Weapon(models.Model):
    item = models.OneToOneField(Item, on_delete=models.CASCADE,
                                related_name='weapon')
    homebrew = models.BooleanField(default=False)
    type = models.ForeignKey(SubType, on_delete=models.CASCADE, blank=True,
                             null=True)
    damage = models.CharField(blank=True, null=True, max_length=10)
    damage_type = models.CharField(blank=True, null=True, max_length=200)
    price = models.CharField(blank=True, null=True, max_length=200)
    weight = models.CharField(blank=True, null=True, max_length=100, default='')
    properties = models.ManyToManyField(Properties, blank=True)
    source = models.CharField(blank=True, null=True, max_length=200)
    description = models.CharField(blank=True, null=True, max_length=3000)
    special = models.CharField(blank=True, null=True, max_length=3000)

    def __str__(self):
        return self.item.name


class Armor(models.Model):
    item = models.OneToOneField(Item, on_delete=models.CASCADE,
                                related_name='armor')
    sub_type = models.ForeignKey(SubType, on_delete=models.CASCADE, blank=True,
                                 null=True, related_name='armor')
    homebrew = models.BooleanField(default=False)
    disadvantage = models.BooleanField(default=False)

    armore = models.CharField(blank=True, null=True, max_length=100)
    duration = models.CharField(blank=True, null=True, max_length=100)
    price = models.CharField(blank=True, null=True, max_length=200)
    weight = models.CharField(blank=True, null=True, max_length=100, default='')
    source = models.CharField(blank=True, null=True, max_length=200)
    description = models.CharField(blank=True, null=True, max_length=3000)
    requirement = models.CharField(blank=True, null=True, max_length=10)

    def __str__(self):
        return self.item.name


class Equipment(models.Model):
    item = models.OneToOneField(Item, on_delete=models.CASCADE,
                                related_name='equipment')
    sub_type = models.ForeignKey(SubType, on_delete=models.CASCADE, blank=True,
                                 null=True, related_name='equipment')
    homebrew = models.BooleanField(default=False)
    price = models.CharField(blank=True, null=True, max_length=200, default='-')
    source = models.CharField(blank=True, null=True, max_length=200,
                              default='-')
    weight = models.CharField(blank=True, null=True, max_length=100,
                              default='-')
    description = models.CharField(blank=True, null=True, max_length=3000,
                                   default='-')

    def __str__(self):
        return self.item.name


class MagicItems(models.Model):
    item = models.OneToOneField(Item, on_delete=models.CASCADE,
                                related_name='magic_item')
    sub_type = models.ForeignKey(SubType, on_delete=models.CASCADE, blank=True,
                                 null=True, related_name='magic_item_type')
    homebrew = models.BooleanField(default=False)
    price = models.CharField(blank=True, null=True, max_length=200, default='-')
    source = models.CharField(blank=True, null=True, max_length=200,
                              default='-')

    customization = models.BooleanField(default=False)
    description = models.CharField(blank=True, null=True, max_length=3000,
                                   default='-')
    detailCustamization = models.CharField(blank=True, null=True,
                                           max_length=200,
                                           default='-')

    detailType = models.CharField(blank=True, null=True, max_length=200,
                                  default='-')

    def __str__(self):
        return self.item.name

    class Meta:
        ordering=['item']



class InventoryItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    character = models.ForeignKey(Character, on_delete=models.CASCADE,
                                  related_name='my_items')
    quantity = models.PositiveIntegerField(default=1)
    put_on = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'инвентарь'
        verbose_name = 'предмет'
        ordering = ['-put_on']

