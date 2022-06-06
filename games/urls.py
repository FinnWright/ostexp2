from django.urls import path
from . import views

urlpatterns = [
    path('', views.AllGames),
    path(r'?q=<str:game_name>/', views.GameHTML),
    path('<str:game_name>/', views.GameHTML)
]