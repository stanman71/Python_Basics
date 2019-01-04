

""" Betrachtet Daten anhand ihrer Nachbarn """


## ##########################
## Teil 0: Einlesen der Daten
## ##########################

import pandas as pd

df = pd.read_csv("./Python_Training/Machine Learning/Klassifikation/CSV/classification.csv")


## ################################################################
## Teil 1: Aufteilung in Trainings- und Testdaten (hier: 75% / 25%)
## ################################################################

from sklearn.model_selection import train_test_split

# Welche Spalten sollen zur Vorhersage verwendet werden
X = df[["age", "interest"]].values

"""  Oder: Die Spalte "success" soll nicht zur Vorhersage verwendet werden:
     X = df.drop("success", axis = 1).values """

y = df["success"].values

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 0, test_size = 0.25)


## ########################
## Teil 2: Daten skallieren
## ########################

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
scaler.fit(X_train)

X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)


## ##########################################
## Teil 3: Nachbarschaftsstrukturen berechnen
## ##########################################

from sklearn.neighbors import KNeighborsClassifier

""" n_neighbors gibt die Anzahl der berücksichtigen Nachbarn an """
model = KNeighborsClassifier(n_neighbors = 15)
model.fit(X_train, y_train)

print(model.score(X_test, y_test))


## ##########################
## Teil 4: Ergebnisse plotten
## ##########################

""" Hinweis: Benötigt plot_classifier.py """

from Support.plot_classifier import plot_classifier

# Trainings-Daten plotten
plot_classifier(model, X_train, y_train, proba = True, xlabel = "Alter", ylabel = "Interesse")

# Testdaten plotten
plot_classifier(model, X_test, y_test, proba = True, xlabel = "Alter", ylabel = "Interesse")


