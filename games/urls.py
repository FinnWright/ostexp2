from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.AllGames),
    re_path(r'?q<str:game_name>/', views.GameHTML),
    path('<str:game_name>/', views.GameHTML)
]