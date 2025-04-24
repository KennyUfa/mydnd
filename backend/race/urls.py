from django.urls import path
from race.views import RaceListView, SubRaceListView, SubRaceChangeView


app_name = 'race'



urlpatterns = [
    path('race-list/', RaceListView.as_view(), name='race-list'),
    path('sub-race-list/<int:pk>/', SubRaceListView.as_view(),
         name='sub-race-list'),
    path('character/<int:pk>/sub-race-change/', SubRaceChangeView.as_view(), name='sub-race-change'),
]
