from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.AllGames),
    path('<str:game_name>/', views.GameHTML)
]