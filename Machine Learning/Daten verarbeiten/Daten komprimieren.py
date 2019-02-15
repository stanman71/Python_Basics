

""" Möglichkeit um Daten zu komprieren und den Informationsverlust abzuschätzen """


## ##########################
## Teil 0: Einlesen der Daten
## ##########################

import pandas as pd

train = pd.read_csv("./Python_Training/Machine Learning/Daten verarbeiten/CSV/train.csv.bz2")
test  = pd.read_csv("./Python_Training/Machine Learning/Daten verarbeiten/CSV/test.csv.bz2")

X_train = train.drop("subject", axis = 1).drop("Activity", axis = 1)
y_train = train["Activity"]

X_test = test.drop("subject", axis = 1).drop("Activity", axis = 1)
y_test = test["Activity"]


## #######################
## Teil 1: Daten skalieren
## #######################

from sklearn.preprocessing import StandardScaler

s = StandardScaler()
X_train = s.fit_transform(X_train)
X_test = s.transform(X_test)


## #########################################
## Teil 2: Daten trainieren und komprimieren
## #########################################

from sklearn.linear_model import LogisticRegression
from sklearn.decomposition import PCA

import numpy as np

p = PCA()
p.fit(X_train)

# Zeigt an, wie viel Varianz wird erfasst wird (hier: erste 100 Einträge)
print(np.sum(p.explained_variance_ratio_[:100]))
