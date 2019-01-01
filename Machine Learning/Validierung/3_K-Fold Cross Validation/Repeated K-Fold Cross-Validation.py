

# Bestimmtheitsmaß mit mehreren Durchläufen

## Teil 0: Einlesen der Daten

import pandas as pd

df = pd.read_csv("./Python_Training/Machine Learning/Validierung/3_K-Fold Cross Validation/CSV/hotels.csv")

df.head()

X = df[["Gewinn", "Quadratmeter"]].values
Y = df[["Preis in Mio"]].values



## Teil 1: Durchführung der Validierung

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import RepeatedKFold

import numpy as np

""" Validierung, hier 5 verschiedene Test- und Trainingsdaten mit 10 Wiederholungen """
scores = cross_val_score(LinearRegression(), X, Y, cv = RepeatedKFold(n_splits = 5, n_repeats = 10))

print(scores)
print(np.mean(scores))




