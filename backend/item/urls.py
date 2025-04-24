from django.urls import path
from rest_framework import routers

from item.views import InventoryItemView, ItemView

router = routers.SimpleRouter()
router.register('items', ItemView, basename='item')
urlpatterns = [

    path('character/<int:character_id>/inventory/<int:pk>/', InventoryItemView.as_view()),
    path('character/<int:character_id>/inventory/', InventoryItemView.as_view()),
]
