from xml.parsers.expat import model
from django.conf import settings
from django.db import models


# Create your models here.
# This file helps add a data table which is called a model in terms of Django's framework. If you want to add a new table
# to store/record data, this file is where you add the table along with its integrity constraints, and attributes.
class Movie(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    release_date = models.DateField()
    runtime_length = models.IntegerField()

    def __str__(self):
        return self.title


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
