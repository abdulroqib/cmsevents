from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('events/', views.events, name='events'),
    path('past-events/', views.past_events, name='past_events'),
    path('events/detail/<id>', views.detail, name='detail')
]