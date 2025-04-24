from django.urls import path, include
from rest_framework import routers

from .views import *

# router = routers.SimpleRouter()
# router.register('prots', ProtectStateView)
# router.register('skillstate', SkillStateView)


urlpatterns = [
    # path('', include(router.urls)),
    # рандомайзер навыков
    path('random-skill/', RandomSaveView.as_view(), name='random'),
    # рандомайзер кубов
    path('random-dice/', RandomDiceView.as_view(), name='random-dice'),
    # ЗДОРОВЬЕ
    path('character/<int:character_id>/max_hit/', MaxHitView.as_view(), name='character-max-hit'),
    path('character/<int:character_id>/heal/', HealPatch.as_view(), name='character-heal'),
    path('character/<int:character_id>/damage/', DamagePatch.as_view(), name='character-damage'),

    path('character/<int:character_id>/possession_bonus/', PossessionBonus.as_view(), name='character-possession-bonus'),
    path('character/<int:character_id>/inspiration_frame/', InspirationBonus.as_view(), name='character-inspiration-bonus'),
    path('character/<int:character_id>/protection_class/', ProtectionClass.as_view(), name='character-protection_class'),
    path('character/<int:character_id>/speed/', Speed.as_view(), name='character-speed'),

]
