

""" An gegebene Datenpunkte soll eine Gerade mit Gleichung y = a + bx so angepasst werden, 
    dass die Summe der Fehlerquadrate minimal wird. """


## ##########################
## Teil 0: Einlesen der Daten
## ##########################

import pandas as pd

df = pd.read_csv("./Python_Training/Machine Learning/Regression/CSV/wohnungspreise.csv")


## ###########################
## Teil 1: Daten visualisieren
## ###########################

import matplotlib.pyplot as plt

plt.scatter(df["Quadratmeter"], df["Verkaufspreis"])
plt.show()


## ###############################
## Teil 2: Berechnung der Funktion
## ###############################

from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(df[["Quadratmeter"]], df[["Verkaufspreis"]])

print("Intercept: " + str(model.intercept_))
print("Coef: " + str(model.coef_))

""" Verkaufspreis = 3143.28481869 + 5071.35242619 * Quadratmeter
    y = 3143.28481869 + 5071.35242619 * x """

print("Preis für 40 QM: " + str(3143.28481869 + 5071.35242619 * 40))


## #######################################
## Teil 3: Abbildung der Regressionsgerade
## #######################################

min_x = min(df["Quadratmeter"])  # erster Wert als Startpunkt
max_x = max(df["Quadratmeter"])  # letzter Wert als Endpunkt

predicted = model.predict([[min_x], [max_x]])

plt.scatter(df["Quadratmeter"], df["Verkaufspreis"])
plt.plot([min_x, max_x], predicted, color = "red")
plt.show()


