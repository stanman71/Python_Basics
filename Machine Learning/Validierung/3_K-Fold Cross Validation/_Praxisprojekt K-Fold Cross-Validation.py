


## Teil 0: Einlesen der Daten

import pandas as pd

df = pd.read_csv("./Python_Training/Machine Learning/Validierung/3_K-Fold Cross Validation/CSV/diamonds.csv")

df.head()



## Teil 1: Durchführung der Validierung (Basis Karat)

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score, RepeatedKFold

X = df[["carat"]].values
Y = df[["price"]].values

""" Validierung, hier 5 verschiedene Test- und Trainingsdaten mit 10 Wiederholungen """
scores = cross_val_score(LinearRegression(), X, Y, cv = RepeatedKFold(n_splits = 5, n_repeats = 10))

import numpy as np

print(np.mean(scores))



## Teil 2: Durchführung der Validierung (Basis Größe)

X = df[["x", "y", "z"]].values
Y = df[["price"]].values

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score, RepeatedKFold

""" Validierung, hier 5 verschiedene Test- und Trainingsdaten mit 10 Wiederholungen """
scores = cross_val_score(LinearRegression(), X, Y, cv = RepeatedKFold(n_splits = 5, n_repeats = 10))

import numpy as np

print(np.mean(scores))


