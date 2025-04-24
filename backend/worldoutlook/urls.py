from django.urls import path, include
from worldoutlook.views import WorldOutlookView, CharacterWorldOutlookView

urlpatterns = [
    path('character/<int:character_id>/world-outlook/', CharacterWorldOutlookView.as_view(),
         name='character-world-outlook'),
    # список мировоззрений
    path('world-outlook-list/', WorldOutlookView.as_view(), name='world-outlook-list'),
    # Список персонажей игрока
]
