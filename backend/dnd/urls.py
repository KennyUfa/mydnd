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
    # обновление способности класса персонажа
    path('character/custom-ability/update/<int:pk>/', CharacterCustomAbilityUpdateView.as_view(), name='custom-ability-update'),
    path('class-list/', BaseClassChViewSet.as_view(), name='class-list'),
    path('race-list/', RaceListView.as_view(), name='race-list'),
    path('origin-list/', OriginListView.as_view(), name='origin-list'),
    # установить выбор происхождения
    path('character/<int:character_id>/origin/', CharacterOriginView.as_view(),
         name='character-origin'),
    # установить выбор мировоззрения
    path('character/<int:character_id>/world-outlook/', CharacterWorldOutlookView.as_view(),
         name='character-world-outlook'),
    # Изменение отображения способности класса
    path('characters/<int:pk>/custom-ability/hide-original/',CharacterHideOriginalAbilityView.as_view(), name='hide-original-ability'),
    # Изменение отображения кастом способности персонажа
    path('characters/<int:pk>/custom-ability/hide-custom/',CharacterHideCustomAbilityView.as_view(), name='hide-custom-ability'),
    # Список персонажей игрока
    path('character-list/', CharacterListView.as_view(), name='character-list'),
    path('characters/create/', CharacterCreateView.as_view(), name='character-create'),
    path('characters/delete/<int:pk>/', CharacterDeleteView.as_view(), name='character-delete'),

    # path('origin/', OriginView.as_view(), name='origin-list'),
    path('random_protect/', RandomSaveView.as_view(), name='random-save'),
    # список мировоззрений
    path('world-outlook-list/', WorldOutlookView.as_view(), name='world-outlook-list'),
    path('characters/<int:character_id>/inventory/', InventoryItemView.as_view()),
    # path('origin/<int:origin_id>/change/', OriginChangeView.as_view(), name='origin-change'),
]
