from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions, filters, status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from character.models import Character
from item.models import Item, InventoryItem
from item.serializers import ItemListsSerializer, ItemsSerializer, InventorySerializer


class ItemView(viewsets.ReadOnlyModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Item.objects.all()
    filter_backends = [filters.SearchFilter, filters.OrderingFilter,
                       DjangoFilterBackend]
    serializer_class = ItemListsSerializer

    def retrieve(self, request, pk=None):
        item = get_object_or_404(Item, pk=pk)
        serializer = ItemsSerializer(item)
        return Response(serializer.data)

    def get_queryset(self):
        query = Q()
        search_query = self.request.query_params.get('search', '')
        rarity_params = self.request.query_params.getlist('rarity[]')
        queryset = Item.objects.all()
        for rarity in rarity_params:
            query |= Q(rarity__id=rarity)

        if search_query:
            query &= Q(name__iregex=search_query)
        queryset = queryset.filter(query).distinct()
        return queryset


class InventoryItemView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, character_id, pk):
        character = get_object_or_404(Character, id=character_id)
        # item_id = request.data.get('item_id')  # Получаем ID предмета
        quantity = request.data.get('quantity', 1)  # Количество (по умолчанию 1)
        # Проверяем, существует ли предмет
        item = get_object_or_404(Item, id=pk)
        # Проверяем, есть ли предмет уже в инвентаре
        inventory_item, created = InventoryItem.objects.get_or_create(
            character=character,
            item=item,
            defaults={'quantity': quantity}  # Если создается новый объект
        )
        if not created:
            # Если предмет уже существует, увеличиваем количество
            inventory_item.quantity += quantity
            inventory_item.save()
        # Сериализуем данные и возвращаем ответ
        serializer = InventorySerializer(inventory_item)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, character_id, pk):
        character = get_object_or_404(Character, id=character_id)
        item = get_object_or_404(Item, id=pk)  # Используем pk из URL
        # Находим предмет в инвентаре
        inventory_item = get_object_or_404(InventoryItem, character=character, item=item)
        # Удаляем предмет
        inventory_item.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self, request, character_id):
        character = get_object_or_404(Character, id=character_id)
        for item in request.data:
            item_id = int(item.get('item').get("id"))
            quantity = int(item.get('quantity'))
            put_on = item.get('put_on')
            inventory_item = get_object_or_404(InventoryItem,
                                               character=character,
                                               item__id=item_id)
            inventory_item.quantity = quantity
            inventory_item.put_on = put_on
            if quantity <= 0:
                inventory_item.delete()
            else:
                inventory_item.save()
        inventory = character.my_items.all()
        serializer = InventorySerializer(inventory, many=True)
        return Response(serializer.data)
