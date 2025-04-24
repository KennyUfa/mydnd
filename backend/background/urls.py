from django.urls import path

from background.views import BackgroundListView, BackgroundChangeView, BackgroundChangeOptionsView, BackgroundChangeOriginView

app_name = 'background'

urlpatterns = [
    path('background-list/', BackgroundListView.as_view(), name='background-list'),
    # установить выбор происхождения
    path('character/<int:pk>/background-change/', BackgroundChangeView.as_view(), name='background-change'),
    path('character/<int:pk>/background-options/', BackgroundChangeOptionsView.as_view(), name='background-change-options'),
    path('character/<int:pk>/background-origin/', BackgroundChangeOriginView.as_view(), name='background-change-origin'),

]
