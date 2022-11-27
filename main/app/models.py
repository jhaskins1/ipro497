from xml.parsers.expat import model
from django.conf import settings
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
# This file helps add a data table which is called a model in terms of Django's framework. If you want to add a new table
# to store/record data, this file is where you add the table along with its integrity constraints, and attributes.

class Genre(models.Model):
    genre = models.CharField(max_length=70)

    def __str__(self):
        return self.genre

class Language(models.Model):
    language = models.CharField(max_length=70)

    def __str__(self):
        return self.language

class Cast(models.Model):
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30)
    role = models.CharField(max_length=70)

    def __str__(self):
        return self.first_name + " " + self.last_name + " as " + self.role

class StreamingOption(models.Model):
    streaming_option = models.CharField('Streaming Options', max_length=70)

    def __str__(self):
        return self.streaming_option

class Movie(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    release_date = models.DateField()
    runtime_length = models.CharField(max_length=8) #HH:MM:SS
    genres = models.ManyToManyField(Genre)
    languages = models.ManyToManyField(Language)
    cast_members = models.ManyToManyField(Cast)
    streaming_options = models.ManyToManyField(StreamingOption, blank=True)
    tmdb_id = models.IntegerField()

    def __str__(self):
        return self.title + " (" + str(self.release_date)[:4] + ")"


class NewVieUser(models.Model):
    username = models.CharField('Username', max_length=30)
    password = models.CharField('Password', max_length=30)
    email = models.EmailField('User Email')

    def __str__(self):
        return self.username

class Rating(models.Model):
    user = models.ForeignKey(NewVieUser)
    movie = models.ForeignKey(Movie)
    rating = models.PositiveSmallIntegerField(validators=[
        MaxValueValidator(5), MinValueValidator(1)]) # Ensures that we will only have ratings between 1 and 5