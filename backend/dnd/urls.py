from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from .views import *

router = routers.SimpleRouter()
router.register('character',CharacterView)
router.register('bc',BaseClassChViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
