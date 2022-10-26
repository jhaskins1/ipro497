import json
import pandas as pd
import numpy as np
import matplotlib as plt
import sklearn
from tmdbv3api import TMDb
from tmdbv3api import Movie


tmdb = TMDb()
tmdb.api_key = '67721f9e029d822c6ca4ab6fd22e7aaf'

movie = Movie()
recommendations = movie.recommendations(movie_id=616037)
testMovies = movie.popular()
movieIDs = []
for i in testMovies:
    movieIDs.append(i["id"])
print(movieIDs)
