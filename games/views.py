from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Game, Song

def AllGames(request):
    return render(request, 'index.html', { 'games' : Game.objects.all() })

def GameHTML(request, game_name):
    game_ = Game.objects.get(name=game_name)

    game_songs = get_object_or_404(Song, game=game_)

    game_songs.sort()

    if (game_songs.count == 0):
        return render(request, 'index.html', { 'games' : Game.objects.all() })

    return render(request, 'songs.html', { 'game_name' : game_name, 'all_songs' : game_songs })
