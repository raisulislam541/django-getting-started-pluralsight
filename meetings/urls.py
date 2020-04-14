from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>', views.details, name='details'),
    path('room', views.room_details, name='room'),
    path('new', views.new, name='new')
]