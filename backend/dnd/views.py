import json

from django.contrib.auth.models import User, Group
from rest_framework import viewsets, views
from rest_framework import permissions, response
from rest_framework.response import Response

from .serializers import UserSerializer, GroupSerializer, CharlistSerializer
from django.contrib import auth
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.http import JsonResponse
from random import randint
from dnd.models import DndSpell, Character
from django.views.generic import ListView


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


def home(request):
    return render(request, 'dnd/home.html')


class CharacterView(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    serializer_class = CharlistSerializer
    queryset = Character.objects.all()
    def get(self, request):
        print(request)
        info = Character.objects.filter(account=self.request.user)
        return Response(CharlistSerializer(info, many=True).data)


def roll_dice(request):
    if request.method == "GET":
        return render(request, 'dnd/dice_roller.html')
    elif request.method == "POST":
        rolls, result = hit_dice_roll(request.POST["amount"], request.POST[
            "dice_type"])
        start_amount = request.POST["amount"]
        start_dice_type = request.POST["dice_type"]

        return render(request, 'dnd/dice_roller.html',
                      {"rolls": rolls, "roll": result, "start": start_amount,
                       'start_dice_type': start_dice_type})


def hit_dice_roll(amount, dice_type):
    rolls = []
    for i in range(int(amount)):
        rolls.append(randint(1, int(dice_type)))
    result = sum(rolls)
    return rolls, result


class SpellView(ListView):
    model = DndSpell


def get_spell(request, spell_id):
    spell = DndSpell.objects.get(id=spell_id)
    return render(request, 'dnd/spell.html', {'spell': spell})


class LoginDnd(LoginView):
    next_page = '/'


def todo(request):
    x = Character.objects.get()
    x.lvl += 1
    x.save()

    return JsonResponse({'lvl': Character.objects.get().lvl}, safe=False)


def testvue(request):
    return render(request, 'todolist.html')
