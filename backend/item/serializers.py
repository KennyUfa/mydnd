from rest_framework import serializers

from item.models import Item, InventoryItem, MagicItems, Armor, Weapon, Equipment, SubType, Rarity, TypeItem, Properties


class PropertiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Properties
        fields = ['name']


class TypeItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeItem
        fields = '__all__'


class RaritySerializer(serializers.ModelSerializer):
    class Meta:
        model = Rarity
        fields = '__all__'


class WeaponTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubType
        fields = '__all__'


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'


class WeaponSerializer(serializers.ModelSerializer):
    item = ItemSerializer()
    properties = PropertiesSerializer(many=True)

    class Meta:
        model = Weapon
        fields = '__all__'

    def to_representation(self, instance):
        data = super(WeaponSerializer, self).to_representation(instance)
        copy_data = data.copy()
        for i in data:
            if not data[i]:
                copy_data.pop(i)
        return copy_data


class EquipmentSerializer(serializers.ModelSerializer):
    item = ItemSerializer()

    class Meta:
        model = Equipment
        fields = '__all__'

    def to_representation(self, instance):
        data = super(EquipmentSerializer, self).to_representation(instance)
        copy_data = data.copy()
        for i in data:
            if not data[i]:
                copy_data.pop(i)
        return copy_data


class ArmorSerializer(serializers.ModelSerializer):
    item = ItemSerializer()

    class Meta:
        model = Armor
        fields = '__all__'

    def to_representation(self, instance):
        data = super(ArmorSerializer, self).to_representation(instance)
        copy_data = data.copy()
        for i in data:
            if not data[i]:
                copy_data.pop(i)
        return copy_data


class MagicItemsSerializer(serializers.ModelSerializer):
    item = ItemSerializer()

    class Meta:
        model = MagicItems
        fields = '__all__'

    def to_representation(self, instance):
        data = super(MagicItemsSerializer, self).to_representation(instance)
        copy_data = data.copy()
        for i in data:
            if not data[i]:
                copy_data.pop(i)
        return copy_data


class ItemListsSerializer(serializers.ModelSerializer):
    rarity = RaritySerializer()
    type = TypeItemSerializer()

    class Meta:
        model = Item
        fields = ['id', 'name', 'rarity', 'type']


class ItemsSerializer(serializers.ModelSerializer):
    rarity = RaritySerializer()
    weapon = WeaponSerializer(allow_null=True)
    armor = ArmorSerializer(allow_null=True)
    equipment = EquipmentSerializer(allow_null=True)
    magic_item = MagicItemsSerializer(allow_null=True)
    type = TypeItemSerializer()

    class Meta:
        model = Item
        fields = '__all__'
        depth = 3

    def to_representation(self, instance):
        data = super(ItemsSerializer, self).to_representation(instance)
        if not data['armor']:
            del data['armor']
        if not data['weapon']:
            del data['weapon']
        if not data['equipment']:
            del data['equipment']
        if not data['magic_item']:
            del data['magic_item']
        return data


class InventorySerializer(serializers.ModelSerializer):
    item = ItemsSerializer()
    quantity = serializers.IntegerField()

    class Meta:
        model = InventoryItem
        fields = "__all__"
