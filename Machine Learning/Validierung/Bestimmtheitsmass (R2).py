

""" Berechnung der Qualität des Modells """


## ##########################
## Teil 0: Einlesen der Daten
## ##########################

import pandas as pd

df = pd.read_csv("./Python_Training/Machine Learning/Validierung/CSV/hotels.csv")

X = df[["Gewinn", "Quadratmeter"]].values
Y = df[["Preis in Mio"]].values


## ################################################################
## Teil 1: Aufteilung in Trainings- und Testdaten (hier: 75% / 25%)
## ################################################################

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, Y, random_state = 0, test_size = 0.25)


## ########################
## Teil 2: Model trainieren
## ########################

from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X_train, y_train)

print(model)

y_test_pred = model.predict(X_test)


## #####################################################
## Teil 3a: Bestimmtheitsmaß berechnen, unabhängiger Weg
## #####################################################

from sklearn.metrics import r2_score

r2 = r2_score(y_test, y_test_pred)
print(r2)

# 0 (sehr schlecht) <<<>>> 1 (perfekt)


## ##############################################################
## Teil 3b: Bestimmtheitsmaß berechnen, während Modell trainieren
## ##############################################################

from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X_train, y_train)

print(model.score(X_test, y_test))

# 0 (sehr schlecht) <<<>>> 1 (perfekt)
