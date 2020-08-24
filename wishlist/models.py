from django.db import models
from django.contrib.auth.models import User


class Movies(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=250)
    year = models.IntegerField()
    summary = models.TextField(max_length=2000)

    class Meta:
        unique_together = ('title', 'year')


class WatchList(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    movie_id = models.OneToOneField(Movies, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    watched = models.BooleanField(default=False)
