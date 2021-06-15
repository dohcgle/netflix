from django.db import models
from .actor import Actor

class Movie(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False)
    year = models.CharField(max_length=4)
    imdb = models.FloatField(default=0, max_length=2, blank=True, null=True)
    genre = models.CharField(max_length=150)
    actor = models.ManyToManyField(Actor)

    def __str__(self):
        return self.name
