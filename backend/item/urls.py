from django.urls import path, include
from rest_framework import routers

from item.views import InventoryItemView, ItemView

app_name = 'item'
router = routers.SimpleRouter()
router.register('items', ItemView, basename='item')
urlpatterns = [
    path('', include(router.urls)),
    path('<int:character_id>/inventory/<int:pk>/', InventoryItemView.as_view()),
    path('<int:character_id>/inventory/', InventoryItemView.as_view()),
]
