from django.urls import path

from . import views

urlpatterns = [
    path("", views.frontier_view, name="frontier"),
]
