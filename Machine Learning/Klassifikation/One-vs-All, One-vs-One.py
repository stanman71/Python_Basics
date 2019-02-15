

""" Klassierung mehrerer Variablen """


## ##########################
## Teil 0: Einlesen der Daten
## ##########################

import pandas as pd

df = pd.read_csv("./Python_Training/Machine Learning/Klassifikation/CSV/foods.csv")

X = df[["energy_100g", "fat_100g", "carbohydrates_100g", "sugars_100g", "proteins_100g"]].values
y = df["clss"].values


## ################################################################
## Teil 1: Aufteilung in Trainings- und Testdaten (hier: 75% / 25%)
## ################################################################

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 42)


## ########################
## Teil 2: Daten skallieren
## ########################

from sklearn.preprocessing import StandardScaler

s = StandardScaler()
s.fit(X_train)

X_train = s.transform(X_train)
X_test = s.transform(X_test)


## #################################
## Teil 3:  One-vs-All (automatisch)
## #################################

""" One-vs-All: Sklearn hat automatisch erkannt, wir möchten hier
                mehrere Klassen vorhersagen - daher wird per default
                die One-vs-all-Methode verwendet. """

from sklearn.linear_model import LogisticRegression

model = LogisticRegression(solver='lbfgs', multi_class='auto')
model.fit(X_train, y_train)

print(model.score(X_test, y_test))


## ###################
## Teil 4:  One-vs-One
## ###################

from sklearn.multiclass import OneVsOneClassifier

model = OneVsOneClassifier(LogisticRegression(solver='lbfgs'))
model.fit(X_train, y_train)

print(model.score(X_test, y_test))


