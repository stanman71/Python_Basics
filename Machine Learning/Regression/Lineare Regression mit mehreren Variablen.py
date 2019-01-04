

## ##########################
## Teil 0: Einlesen der Daten
## ##########################


import pandas as pd

df = pd.read_csv("./Python_Training/Machine Learning/Regression/CSV/hotels.csv")

X = df[["Gewinn", "Quadratmeter"]].values
Y = df[["Preis in Mio"]].values


## ################################################################
## Teil 1: Aufteilung in Trainings- und Testdaten (hier: 75% / 25%)
## ################################################################

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

X_train, X_test, y_train, y_test = train_test_split(X, Y, random_state = 0, test_size = 0.25)


## ########################
## Teil 2: Model trainieren
## ########################

model = LinearRegression()
model.fit(X_train, y_train)

print(model.intercept_)
print(model.coef_)

# 6.48370247 + [Gewinn] * 6.39855984e-06 + [Quadrameter] * 3.89642288e-03


## ###########################################################################
## Teil 3: Ausgabe der Ergebnisse (berechnete Ergebnisse vs. reale Ergebnisse)
## ###########################################################################

y_test_pred = model.predict(X_test)

for i in range(0, len(y_test_pred)):
    print("Berechnet: " + str(y_test_pred[i][0]) + " - Real: " + str(y_test[i][0]))


