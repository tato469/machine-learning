# Common imports
import numpy as np
import os
import pandas as pd

TITANIC_PATH = os.path.join("datasets")
TEST = "test.csv"
TRAIN = "train.csv"
EVALUATE = "gender_submission.csv"


#Funtion for load a dataset
# @return pandas-dataframe
def load_titanic_data(dataset,path=TITANIC_PATH):
    csv_path = os.path.join(path, dataset)
    return pd.read_csv(csv_path)


#Loading datasets
titanic = load_titanic_data(TRAIN)
titanic_test = load_titanic_data(TEST)
titanic_labels = titanic["Survived"].copy()
titanic_evaluate = load_titanic_data(EVALUATE)

print()
