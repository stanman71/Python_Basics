

""" Ein Random Forest ist ein Klassifikationsverfahren, das aus mehreren unkorrelierten 
    Entscheidungsbäumen besteht. 
    Alle Entscheidungsbäume sind unter einer bestimmten Art von Randomisierung während 
    des Lernprozesses gewachsen. """


## ##########################
## Teil 0: Einlesen der Daten
## ##########################

import pandas as pd

df = pd.read_csv("./Python_Training/Machine Learning/Entscheidungsbaum/CSV/classification.csv")


## ################################################################
## Teil 1: Aufteilung in Trainings- und Testdaten (hier: 75% / 25%)
## ################################################################

from sklearn.model_selection import train_test_split

# Welche Spalten sollen zur Vorhersage verwendet werden
X = df[["age", "interest"]].values

""" Oder: Die Spalte "success" soll nicht zur Vorhersage verwendet werden:
    X = df.drop("success", axis = 1).values """

y = df["success"].values

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 0, test_size = 0.25)


## ###########################
## Teil 2: Random Forest bauen
## ###########################

from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(criterion = "entropy", n_estimators = 30)
model.fit(X_train, y_train)

print(model.score(X_test, y_test))


## #############################
## Teil 3: Random Forest plotten
## #############################

""" Hinweis: Benötigt plot_classifier.py """

from plot_classifier import plot_classifier

# Trainings-Daten plotten
plot_classifier(model, X_train, y_train, proba = True, xlabel = "Alter", ylabel = "Interesse")

# Testdaten plotten
plot_classifier(model, X_test, y_test, proba = True, xlabel = "Alter", ylabel = "Interesse")

