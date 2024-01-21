import re

from django.db.models import Q
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets, permissions, status, generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import *


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class BaseClassChViewSet(generics.ListAPIView):
    queryset = ClassChampion.objects.all()
    serializer_class = BaseClassChSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return ClassChampion.objects.all()


class RaceViewSet(generics.ListAPIView):
    queryset = Race.objects.all()
    serializer_class = RaceSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Race.objects.all()


class CharacterView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CharacterSerializer
    queryset = Character.objects.all()

    def get_queryset(self):
        return Character.objects.filter(account=self.request.user)


class SpellView(viewsets.ReadOnlyModelViewSet):
    queryset = Spell.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter,
                       DjangoFilterBackend]
    serializer_class = SpellBookSerializer


    def retrieve(self, request, pk=None):
        spell = get_object_or_404(Spell, pk=pk)
        serializer = ChampionSpellSerializer(spell)
        return Response(serializer.data)

    def get_queryset(self):

        search_query = self.request.query_params.get('search', '')
        queryset = Spell.objects.all()

        if search_query:
            print(search_query)
            queryset = queryset.filter(name__iregex=search_query.strip())
        return queryset


class BackgroundView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = BackgroundSerializer
    queryset = BackgroundModel.objects.all()


class ProtectStateView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProtectStateSerializer
    queryset = ProtectStateModel.objects.all()


class SkillStateView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = SkillStateSerializer
    queryset = SkillStateModel.objects.all()


class OriginView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Origin.objects.all()
    serializer_class = OriginChoiceSerializer

    def get_queryset(self):
        return Origin.objects.all()


class WorldOutlookView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = WorldOutlook.objects.all()
    serializer_class = WorldOutlookSerializer

    def get_queryset(self):
        return WorldOutlook.objects.all()


class ItemView(viewsets.ReadOnlyModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Item.objects.all()
    filter_backends = [filters.SearchFilter, filters.OrderingFilter,
                       DjangoFilterBackend]
    serializer_class = ItemsSerializer

    def retrieve(self, request, pk=None):
        item = get_object_or_404(Item, pk=pk)
        serializer = ItemsSerializer(item)
        return Response(serializer.data)

    def get_queryset(self):
        search_query = self.request.query_params.get('search', '')
        queryset = Item.objects.all()
        if search_query:
            queryset = queryset.filter(name__icontains=search_query)
        return queryset


class InventoryItemView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, character_id):
        character = get_object_or_404(Character, id=character_id)
        item_id = request.data.get('item_id')
        quantity = request.data.get('quantity', 1)
        item = get_object_or_404(Item, id=item_id)
        inventory_item, created = InventoryItem.objects.get_or_create(
            character=character, item=item)
        if not created:
            inventory_item.quantity = quantity
        else:
            inventory_item.quantity = quantity
        inventory_item.save()
        serializer = InventorySerializer(inventory_item)
        return Response(serializer.data)

    def delete(self, request, character_id):
        character = get_object_or_404(Character, id=character_id)
        item_id = request.data.get('item_id')
        item = get_object_or_404(Item, id=item_id)
        inventory_item = get_object_or_404(InventoryItem,
                                           character=character, item=item)
        inventory_item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self, request, character_id):
        character = get_object_or_404(Character, id=character_id)
        for item in request.data.get('my_items'):
            item_id = int(item.get('item').get("id"))
            quantity = int(item.get('quantity'))
            inventory_item = get_object_or_404(InventoryItem,
                                               character=character,
                                               item__id=item_id)
            inventory_item.quantity = quantity
            if quantity <= 0:
                inventory_item.delete()
            else:
                inventory_item.save()
        inventory = character.my_items.all()
        serializer = InventorySerializer(inventory, many=True)
        return Response(serializer.data)


class OriginChangeView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def patch(self, request, origin_id):
        id = request.data.get('character_id')
        character = get_object_or_404(Character, id=id)
        origin = get_object_or_404(Origin, id=origin_id)
        character.my_origin = origin
        character.save()
        serializer = CharacterSerializer(character)
        return Response(serializer.data)
