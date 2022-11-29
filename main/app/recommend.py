# This is the actual recommendation algorithm.
# DESCRIPTION: WIP

#still unfinished, but this should be closer to how it needs to work

# install scikit-surprise 
#not sure if this is how it should be done
#instructions just said to use command line?
from collections import defaultdict
import numpy as np 
import pandas as pd
from scipy import spatial
# from app.models import Rating
from surprise import accuracy, SVD, Dataset, Reader
from surprise.model_selection import cross_validate
from surprise.model_selection import train_test_split
import os

from tmdbv3api import TMDb
from tmdbv3api import Movie


tmdb = TMDb()
tmdb.api_key = '67721f9e029d822c6ca4ab6fd22e7aaf'

movie = Movie()
pop = movie.popular()
# for i in pop:
    # print(i.title)

df = pd.read_csv("ipro497\\main\\app\\data\\links.csv", index_col= 0, usecols=[0,2])

#returns reclist, a dict where keys are user ids, values are lists of tuples
#[(item id, rating estimate), ...] of size n (default 10)
#taken from scikit surprise examples, edited for the purpose of this program

def MyRecs(predictions, n=10):
    
    reclist = defaultdict(list)

    for uid, iid, true_r, est, _ in predictions:
        reclist[uid].append((iid, est))
    
    for uid, user_ratings in reclist.items():
        user_ratings.sort(key=lambda x: x[1], reverse=True)
        reclist[uid] = user_ratings[:n]
    
    return reclist

file_path = os.path.expanduser("ipro497\\main\\app\\data\\ratings_100.csv") #ADD DATASET FILE TO THIS

reader = Reader(line_format = "user item rating timestamp", sep =',', skip_lines=1)
data = Dataset.load_from_file(file_path, reader = reader)
trainset = data.build_full_trainset()
algo = SVD()
algo.fit(trainset)

# Than predict ratings for all pairs (u, i) that are NOT in the training set.
testset = trainset.build_anti_testset()
predictions = algo.test(testset)

top_n = MyRecs(predictions, n=10)
# Print the recommended items for each user
for uid, user_ratings in top_n.items():
    if uid == '600':
        print(uid, [int(df['tmdbId'][int(iid)]) for (iid, _) in user_ratings])

