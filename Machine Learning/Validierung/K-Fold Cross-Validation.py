

""" Erweiterung des Bestimmheitsmaßes für stabilere Ergebnisse
    (Durchschnitt aus mehreren Aufteilungen der Test- und Trainingsdaten) """


## ##########################
## Teil 0: Einlesen der Daten
## ##########################

import pandas as pd

df = pd.read_csv("./Python_Training/Machine Learning/Validierung/CSV/hotels.csv")

X = df[["Gewinn", "Quadratmeter"]].values
Y = df[["Preis in Mio"]].values


## ###################################
## Teil 1: Validierung (ein Durchlauf)
## ###################################

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold

import numpy as np

""" Validierung, hier 10 verschiedene Test- und Trainingsdaten """
scores = cross_val_score(LinearRegression(), X, Y, cv = KFold(n_splits = 10))

print("ein Durchlauf")
print(scores)
print(np.mean(scores))


## ########################################
## Teil 2: Validierung (mehrere Durchläufe)
## ########################################

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import RepeatedKFold

import numpy as np

""" Validierung, hier 5 verschiedene Test- und Trainingsdaten mit 10 Wiederholungen """
scores = cross_val_score(LinearRegression(), X, Y, cv = RepeatedKFold(n_splits = 5, n_repeats = 10))

print("mehrere Durchläufe")
print(scores)
print(np.mean(scores))
