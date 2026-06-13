from django.urls import path
from . import views

urlpatterns = [
    path('', views.game_view, name='game'),
    path('messages/', views.messages, name='messages'),
]
