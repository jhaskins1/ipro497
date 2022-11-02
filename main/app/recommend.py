# This is the actual recommendation algorithm.
# DESCRIPTION: WIP

install scikit-surprise 
#not sure if this is how it should be done
#instructions just said to use command line?

import numpy as np 
import pandas as pd
from surprise import Dataset
from surprise import Reader
from surprise import 
#maybe import other stuff from surprise
from scipy import spatial
from app.models import Rating #need updated database


#returns reclist, the list of n recommended movies
def MyRecs():
    
    #okay still figuring this out
    #but essentially we need to use SVD from scikit-surprise
    #using the dataset we have from tmdb
    #and then use that output to create a list of the n recommended movies
    #which is then returned
    
    return reclist


