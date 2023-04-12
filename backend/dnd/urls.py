from django.urls import path, include
from rest_framework import routers

from .views import *

router = routers.SimpleRouter()
router.register('character', CharacterView)
router.register('prots', ProtectStateView)
router.register('skillstate', SkillStateView)
router.register('spell', SpellView, basename='spell')


urlpatterns = [
    path('', include(router.urls)),
    path('classlist/', BaseClassChViewSet.as_view(), name='class-list'),
    path('racelist/', RaceViewSet.as_view(), name='race-list'),
    path('prehistory/', PreHistoryView.as_view(), name='pre-history-list'),
    path('looklist/', WorldOutlookView.as_view(), name='world-outlook-list'),
    path('item/',ItemAPIView.as_view())
]
