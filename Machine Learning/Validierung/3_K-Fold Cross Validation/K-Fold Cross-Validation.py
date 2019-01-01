


# Erweiterung des Bestimmheitsmaßes für stabilere Ergebnisse
# (Durchschnitt aus mehreren Aufteilungen der Test- und Trainingsdaten)

## Teil 0: Einlesen der Daten

import pandas as pd

df = pd.read_csv("./Python_Training/Machine Learning/Validierung/3_K-Fold Cross Validation/CSV/hotels.csv")

df.head()

X = df[["Gewinn", "Quadratmeter"]].values
Y = df[["Preis in Mio"]].values



## Teil 1: Durchführung der Validierung

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold

import numpy as np

""" Validierung, hier 10 verschiedene Test- und Trainingsdaten """
scores = cross_val_score(LinearRegression(), X, Y, cv = KFold(n_splits = 10))

print(scores)
print(np.mean(scores))


