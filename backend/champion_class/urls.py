from django.urls import path

from champion_class.views import BaseClassChViewSet, ArchetypeViewSet, ArchetypeChangeView, CharacterHideOriginalAbilityView, \
    CharacterHideCustomAbilityView, CharacterCustomAbilityUpdateView, Archetypes

app_name = 'champion_class'

urlpatterns = [
    path('class-list/', BaseClassChViewSet.as_view(), name='class-list'),
    path('archetypes/', Archetypes.as_view(), name='archetypes-list'),
    path('class-archetype-list/<int:pk>/', ArchetypeViewSet.as_view(), name='archetype-list'),
    path('character/<int:pk>/archetype-change/', ArchetypeChangeView.as_view(), name='archetype-change'),
    # Изменение отображения способности класса
    path('characters/<int:pk>/custom-ability/hide-original/', CharacterHideOriginalAbilityView.as_view(), name='hide-original-ability'),
    # Изменение отображения кастом способности персонажа
    path('characters/<int:pk>/custom-ability/hide-custom/', CharacterHideCustomAbilityView.as_view(), name='hide-custom-ability'),
    path('character/custom-ability/update/<int:pk>/', CharacterCustomAbilityUpdateView.as_view(), name='custom-ability-update'),
]
