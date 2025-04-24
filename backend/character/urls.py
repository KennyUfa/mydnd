from django.urls import path

from .views import *

app_name = 'character'

urlpatterns = [

    path('<int:pk>/', CharacterDetailView.as_view(), name='character-detail'),
    # установить выбор характеристик класса персонажа
    path('<int:pk>/skills/', CharacterSkillsView.as_view(),
         name='character-skills'),
    # установить выбор способностей класса персонажа
    path('<int:pk>/skill_state/', CharacterSkillStateView.as_view(), name='character-skill-state'),
    # установить Спасброски
    path('<int:pk>/protect_state/', CharacterProtectStateView.as_view(), name='character-protect_state'),
    # установить выбор мировоззрения
    path('character-list/', CharacterListView.as_view(), name='character-list'),
    path('create/', CharacterCreateView.as_view(), name='character-create'),
    path('delete/<int:pk>/', CharacterDeleteView.as_view(), name='character-delete'),

]
