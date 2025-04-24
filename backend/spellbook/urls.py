from poplib import POP3_SSL

from django.urls import path, include
from rest_framework import routers

from spellbook.views import SpellSearchView, SpellBookPatch, SpellBookSlotPatch, SpellView

app_name = 'spellbook'

router = routers.SimpleRouter()
router.register('spellbook', SpellView, basename='spellbook')




urlpatterns = [

    path('search/', SpellSearchView.as_view(), name='spellbook-search'),
    path('<int:character_id>/patch/', SpellBookPatch.as_view(), name='spellbook-patch'),
    path('<int:character_id>/slot/patch/', SpellBookSlotPatch.as_view(), name='spellbook-slot-patch'),

]
