# This is the actual recommendation algorithm.
# DESCRIPTION: WIP

#still unfinished, but this should be closer to how it needs to work

install scikit-surprise 
#not sure if this is how it should be done
#instructions just said to use command line?

import numpy as np 
import pandas as pd
from scipy import spatial
from app.models import Rating
from surprise import SVD
from surprise import Dataset
from surprise import Reader
from surprise.model_selection import cross_validate
import os



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

file_path = os.path.expanduser("dataset file goes here") #ADD DATASET FILE TO THIS

reader = Reader(line_format = "format of data file", sep ="seperating character")

data = Dataset.load_from_file(file_path, reader = reader)

trainset = data.build_full_trainset()
algo = SVD()
algo.fit(trainset)

testset = trainset.build_anti_testset()
predictions = algo.test(testset)

reclist = gMyRecs(predictions, n=10)


