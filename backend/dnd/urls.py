from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from .views import *

router = routers.SimpleRouter()
router.register('character',CharacterView)


urlpatterns = [
    path('', include(router.urls)),
]
