from telnetlib import GA
from django.db import models

class Game(models.Model):
    img = models.CharField(max_length=2083)
    name = models.CharField(max_length=255)
    song_count = models.IntegerField()
    description = models.CharField(max_length=2083)
    color = models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.name

class Song(models.Model):
    img = models.CharField(max_length=2083)
    name = models.CharField(max_length=255)
    ost_index = models.IntegerField()
    description = models.CharField(max_length=2083)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    color = models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.name


    def __lt__(self, other):
        return self.ost_index < other.ost_index