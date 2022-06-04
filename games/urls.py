from django.urls import path
from . import views

urlpatterns = [
    path('', views.AllGames),
    path('<str:game_name>/', views.GameHTML)
]