

""" Machen mehr Daten das Modell genauer ? """


## ##########################
## Teil 0: Einlesen der Daten
## ##########################

import pandas as pd

df = pd.read_csv("./Python_Training/Machine Learning/Validierung/CSV/classification.csv")

X = df[["age", "interest"]].values
y = df["success"].values


## ########################
## Teil 1: Model trainieren
## ########################

from sklearn.model_selection import learning_curve
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import RepeatedStratifiedKFold
from sklearn.preprocessing import StandardScaler
from sklearn.utils import shuffle

import numpy as np

X, y = shuffle(X, y)

train_sizes_abs, train_scores, test_scores = learning_curve(
    LogisticRegression(solver='lbfgs', C = 1000000), X, y, cv = RepeatedStratifiedKFold(n_repeats = 1000))


## ##########################
## Teil 2: Ergebnisse plotten
## ##########################

import matplotlib.pyplot as plt

plt.plot(train_sizes_abs, np.median(train_scores, axis = 1))
plt.plot(train_sizes_abs, np.median(test_scores, axis = 1))

plt.show()

""" Blaue  Linie: Training Score 
    Orange Linie: Test Score 
    
    X = Anzahl Daten 
    Ziel: Kurven annähren, müssen sich aber nicht zwingend treffen """
