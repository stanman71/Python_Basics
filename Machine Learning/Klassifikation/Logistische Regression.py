

""" Unter logistischer Regression oder Logit-Modell versteht man Regressionsanalysen zur 
    Modellierung der Verteilung abhängiger zufälliger (diskreter) Variablen und Zuordnung 
    zu einer Klasse.
    Ziel: Kurvenverlauf mit möglichst geringen Abstand zu den einezlnen Punkten """


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

""" Oder: Die Spalte "success" soll nicht zur Vorhersage verwendet werden:
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
X_test  = scaler.transform(X_test)


## #########################
## Teil 3: Modell trainieren 
## #########################

from sklearn.linear_model import LogisticRegression

model = LogisticRegression(solver='lbfgs')
model.fit(X_train, y_train)

# Güte des Modells
print(model.score(X_test, y_test))


## ##########################
## Teil 4: Ergebnisse plotten
## ##########################

""" Hinweis: Benötigt plot_classifier.py """

from Support.plot_classifier import plot_classifier

# Trainings-Daten plotten (proba bezieht sich auf die Visualisierung der Grenze)
plot_classifier(model, X_train, y_train, proba = True, xlabel = "Alter", ylabel = "Interesse")

# Testdaten plotten (proba bezieht sich auf die Visualisierung der Grenze)
plot_classifier(model, X_test, y_test, proba = True, xlabel = "Alter", ylabel = "Interesse")

