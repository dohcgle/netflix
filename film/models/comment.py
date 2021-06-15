from django.db import models
from .movie import Movie
from django.contrib.auth import get_user_model

User = get_user_model()

class Comment(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateField()


