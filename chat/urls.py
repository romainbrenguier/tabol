from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('game/<str:lang_code>/', views.game_view, name='game'),
    path('messages/', views.messages, name='messages'),
]
