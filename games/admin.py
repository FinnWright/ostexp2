from django.contrib import admin
from .models import Game, Song

class GameAdmin(admin.ModelAdmin):
    list_display = ('name', 'song_count', 'description')

class SongAdmin(admin.ModelAdmin):
    list_display = ('game', 'name', 'ost_index', 'description')

admin.site.register(Game, GameAdmin)
admin.site.register(Song, SongAdmin)
