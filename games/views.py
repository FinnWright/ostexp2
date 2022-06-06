from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Game, Song

def AllGames(request):
    return render(request, 'index.html', { 'games' : Game.objects.all() })

def GameHTML(request, game_name):
    if (not Game.objects.filter(name=game_name).exists()):
        return render(request, 'index.html', { 'games' : Game.objects.all() })

    game_ = Game.objects.get(name=game_name)

    game_songs = Song.objects.filter(game=game_).order_by('ost_index')

    return render(request, 'songs.html', { 'game_name' : game_name, 'all_songs' : game_songs })
