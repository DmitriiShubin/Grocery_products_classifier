#import libs

#data processing
import pandas as pd
import numpy as np
from scipy.spatial.distance import cosine
import pickle

#models
from sklearn.neighbors import KNeighborsClassifier

#web
from fastapi import FastAPI

#support
import logging
import time
import mlflow


logging.basicConfig(filename='./logs/result.log',format='%(asctime)s - %(message)s', level=logging.INFO)



#define model names
MDOEL_PATH = './models/lexvec/weights/'
MDOEL_NAME = f'{MDOEL_PATH}lexvec.bin'

#define data names
DATA_PATH = './data/'
DATA_NAME = f'{DATA_PATH}product_list.csv'
TEST_DATA = f'{DATA_PATH}test_list.csv'

#number of splits for pdediction, please refere to README.md
N_SPLITS = 1

