

""" Sucht automatisch aus einer vorgegebenen Liste die optimalen Parameter (z.B. C, gamma) """


## ##########################
## Teil 0: Einlesen der Daten
## ##########################

import pandas as pd

df = pd.read_csv("./Python_Training/Machine Learning/Validierung/CSV/classification.csv")


## ################################################################
## Teil 1: Aufteilung in Trainings- und Testdaten (hier: 75% / 25%)
## ################################################################

from sklearn.model_selection import train_test_split

X = df[["age", "interest"]].values
y = df["success"].values

X_train, X_test, y_train, y_test = train_test_split(X, y)


## #################################
## Teil 2: Erstellung einer Pipeline
## #################################

from sklearn.pipeline import Pipeline

from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier

pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("knn", KNeighborsClassifier(n_neighbors=""))
])


## ################################
## Teil 3: Durchtesten der Pipeline
## ################################

from sklearn.model_selection import GridSearchCV

""" Automatische Trennung in Trainings- und Validierungsdaten 
    Testet alle angebenen Werte und gibt den optimalen Wert aus """

clf = GridSearchCV(pipeline, param_grid = {
    "knn__n_neighbors": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
})
clf.fit(X_train, y_train)

# bester Hyperparameter
print(clf.best_params_)

# Score Validierungsdaten 
# (oft höher als bei Testdaten, da Hyperparameter darauf optimiert wurde)
print(clf.best_score_)

# Score Testdaten
print(clf.score(X_test, y_test))
