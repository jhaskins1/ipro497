from xml.parsers.expat import model
from django.conf import settings
from django.db import models


# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    release_date = models.DateField()
    runtime_length = models.IntegerField()


class Genre(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    genre = models.CharField(max_length=70)

class Language(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    language = models.CharField(max_length=70)

class Cast(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    name = models.CharField(max_length=70)
    role = models.CharField(max_length=70)

class StreamingOption(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    streaming_option = models.CharField('Streaming Options', max_length=70)
