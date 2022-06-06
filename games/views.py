from django.shortcuts import render
from django.http import HttpResponse
from .models import Game, Song
import logging

def AllGames(request):
    return render(request, 'index.html', { 'games' : Game.objects.all() })

def GameHTML(request, game_name):
    allsongs = Song.objects.all()
    game_songs = []

    for song in allsongs:
        if song.game.name == game_name:
            game_songs.append(song)

    game_songs.sort()

    logging.basicConfig(level=logging.INFO)
    logging.debug(game_name + game_songs.count)

    #Problem Area:
    if (game_songs.count == 0):
        return render(request, 'index.html', { 'games' : Game.objects.all() })

    return render(request, 'songs.html', { 'game_name' : game_name, 'all_songs' : game_songs})
