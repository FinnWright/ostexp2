from django.shortcuts import render
from django.http import HttpResponse
from .models import Game, Song

def AllGames(request):
    games = Game.objects.all()
    return render(request, 'index.html', { 'games' : games})

def GameHTML(request, game_name):
    allsongs = Song.objects.all()
    game_songs = []

    for song in allsongs:
        if song.game.name == game_name:
            game_songs.append(song)

    game_songs.sort()

    if (game_songs.count == 0):
        return render(request, 'index.html', { 'games' : Game.objects.all() })
    return render(request, 'songs.html', { 'game_name' : game_name, 'all_songs' : game_songs})
