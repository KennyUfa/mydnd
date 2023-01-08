from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from .views import *

router = routers.SimpleRouter()
router.register('character', CharacterView)


urlpatterns = [
    path('', include(router.urls)),
    path('classlist/', BaseClassChViewSet.as_view(), name='class-list'),
    path('racelist/', RaceViewSet.as_view(), name='race-list'),
]
