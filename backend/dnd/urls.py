from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from .views import *

# router = routers.DefaultRouter()
# router.register('dnd', CharacterView, 'dnd')
#

urlpatterns = [
    #     path('roll/', roll_dice, name='roll'),
    #     path('spells/', SpellView.as_view(), name='spells'),
    #     path('spells/<int:spell_id>/', get_spell, name='spell'),
    path('character/', CharacterView.as_view({'get':'get'}), name='character'),
    # path('todo/', testvue, name='todo'),
]
