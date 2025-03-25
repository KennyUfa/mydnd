from django.urls import path, include
from rest_framework import routers

from .views import *

router = routers.SimpleRouter()
# router.register('character', CharacterListView)
router.register('prots', ProtectStateView)
router.register('skillstate', SkillStateView)
router.register('spell', SpellView, basename='spell')
router.register('items', ItemView, basename='item')
# router.register('character', CharacterView, basename='character')


urlpatterns = [
    path('', include(router.urls)),
    path('character/<int:pk>/', CharacterDetailView.as_view(), name='character-detail'),

    path('class-list/', BaseClassChViewSet.as_view(), name='class-list'),
    path('class-archetype-list/<int:pk>/', ArchetypeViewSet.as_view(), name='archetype-list'),
    path('character/<int:pk>/archetype-change/', ArchetypeChangeView.as_view(), name='archetype-change'),

    path('race-list/', RaceListView.as_view(), name='race-list'),
    path('sub-race-list/<int:pk>/', SubRaceListView.as_view(),
         name='sub-race-list'),
    path('character/<int:pk>/sub-race-change/', SubRaceChangeView.as_view(), name='sub-race-change'),

    path('background-list/', BackgroundListView.as_view(), name='background-list'),
    # установить выбор происхождения
    path('character/<int:pk>/background-change/', BackgroundChangeView.as_view(), name='background-change'),
    path('character/<int:pk>/background-options/', BackgroundChangeOptionsView.as_view(), name='background-change-options'),
    path('character/<int:pk>/background-origin/', BackgroundChangeOriginView.as_view(), name='background-change-origin'),

    # установить выбор характеристик класса персонажа
    path('character/<int:pk>/skills/', CharacterSkillsView.as_view(),
         name='character-skills'),
    # установить выбор способностей класса персонажа
    path('character/<int:pk>/skill_state/', CharacterSkillStateView.as_view(), name='character-skill-state'),
    # установить Спасброски
    path('character/<int:pk>/protect_state/', CharacterProtectStateView.as_view(), name='character-protect_state'),
    # установить выбор мировоззрения
    path('character/<int:character_id>/world-outlook/', CharacterWorldOutlookView.as_view(),
         name='character-world-outlook'),
    # Изменение отображения способности класса
    path('characters/<int:pk>/custom-ability/hide-original/', CharacterHideOriginalAbilityView.as_view(), name='hide-original-ability'),
    # Изменение отображения кастом способности персонажа
    path('characters/<int:pk>/custom-ability/hide-custom/', CharacterHideCustomAbilityView.as_view(), name='hide-custom-ability'),
    # Список персонажей игрока
    path('character-list/', CharacterListView.as_view(), name='character-list'),
    path('characters/create/', CharacterCreateView.as_view(), name='character-create'),
    path('characters/delete/<int:pk>/', CharacterDeleteView.as_view(), name='character-delete'),

    # path('origin/', OriginView.as_view(), name='origin-list'),
    path('random_protect/', RandomSaveView.as_view(), name='random'),
    # список мировоззрений
    path('world-outlook-list/', WorldOutlookView.as_view(), name='world-outlook-list'),

    path('character/<int:character_id>/inventory/<int:pk>/', InventoryItemView.as_view()),
    path('character/<int:character_id>/inventory/', InventoryItemView.as_view()),

    # обновление способности класса персонажа
    path('character/custom-ability/update/<int:pk>/', CharacterCustomAbilityUpdateView.as_view(), name='custom-ability-update'),
    # Заклинания
    path('spells/search/', SpellSearchView.as_view(), name='spell-search'),
    path('<int:character_id>/spellbook/patch/', SpellBookPatch.as_view(), name='spellbook-patch'),
    path('<int:character_id>/spellbook/slot/patch/', SpellBookSlotPatch.as_view(), name='spellbook-slot-patch'),
    path('archetypes/', Archetypes.as_view(), name='archetypes-list'),

]
