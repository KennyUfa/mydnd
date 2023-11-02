from django.urls import path, include
from rest_framework import routers

from .views import *

router = routers.SimpleRouter()
router.register('character', CharacterView)
router.register('prots', ProtectStateView)
router.register('skillstate', SkillStateView)
router.register('spell', SpellView, basename='spell')
router.register('items', ItemView, basename='item')

urlpatterns = [
    path('', include(router.urls)),
    path('classlist/', BaseClassChViewSet.as_view(), name='class-list'),
    path('racelist/', RaceViewSet.as_view(), name='race-list'),
    path('origin/', OriginView.as_view(), name='origin-list'),
    path('looklist/', WorldOutlookView.as_view(), name='world-outlook-list'),
    path('characters/<int:character_id>/inventory/', InventoryItemView.as_view()),
    path('origin/<int:origin_id>/change/', OriginChangeView.as_view(), name='origin-change'),
]
