from django.urls import path

from .views import *

# router = routers.SimpleRouter()
# router.register('prots', ProtectStateView)
# router.register('skillstate', SkillStateView)
app_name = 'character'

urlpatterns = [
    # path('', include(router.urls)),
    path('character/<int:pk>/', CharacterDetailView.as_view(), name='character-detail'),
    # установить выбор характеристик класса персонажа
    path('character/<int:pk>/skills/', CharacterSkillsView.as_view(),
         name='character-skills'),
    # установить выбор способностей класса персонажа
    path('character/<int:pk>/skill_state/', CharacterSkillStateView.as_view(), name='character-skill-state'),
    # установить Спасброски
    path('character/<int:pk>/protect_state/', CharacterProtectStateView.as_view(), name='character-protect_state'),
    # установить выбор мировоззрения
    path('character-list/', CharacterListView.as_view(), name='character-list'),
    path('characters/create/', CharacterCreateView.as_view(), name='character-create'),
    path('characters/delete/<int:pk>/', CharacterDeleteView.as_view(), name='character-delete'),
    #
    # # ЗДОРОВЬЕ
    # path('character/<int:character_id>/max_hit/', MaxHitView.as_view(), name='character-max-hit'),
    # path('character/<int:character_id>/heal/', HealPatch.as_view(), name='character-heal'),
    # path('character/<int:character_id>/damage/', DamagePatch.as_view(), name='character-damage'),
    #
    # path('character/<int:character_id>/possession_bonus/', PossessionBonus.as_view(), name='character-possession-bonus'),
    # path('character/<int:character_id>/inspiration_frame/', InspirationBonus.as_view(), name='character-inspiration-bonus'),
    # path('character/<int:character_id>/protection_class/', ProtectionClass.as_view(), name='character-protection_class'),
    # path('character/<int:character_id>/speed/', Speed.as_view(), name='character-speed'),

]
