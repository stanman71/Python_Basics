

""" Ausgabe der Daten in verschiedenen Ansätzen zur besseren Verständlichkeit """


## ##########################
## Teil 0: Einlesen der Daten
## ##########################

import pandas as pd

df = pd.read_csv("./Python_Training/Machine Learning/Klassifikation/CSV/classification.csv")


## ################################################################
## Teil 1: Aufteilung in Trainings- und Testdaten (hier: 75% / 25%)
## ################################################################

from sklearn.model_selection import train_test_split

X = df[["age", "interest"]].values
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


## #############################################
## Teil 3: Ergebnisse der Trainingsdaten plotten
## #############################################

import matplotlib.pyplot as plt

plt.scatter(X_train[:, 0], X_train[:, 1], c=y_train)
plt.xlabel("Alter")
plt.ylabel("Interesse")
plt.show()


## ##################################
## Teil 4: Bestimmtheitsmaß berechnen
## ##################################

from sklearn.linear_model import LogisticRegression

model = LogisticRegression()
model.fit(X_train, y_train)

print(model.score(X_test, y_test))

y_predicted = model.predict(X_test)


## ########################################
## Teil 5: Ergebnisse der Testdaten plotten
## ########################################

import matplotlib.pyplot as plt

plt.scatter(X_test[:, 0], X_test[:, 1], c=y_test)
plt.xlabel("Alter")
plt.ylabel("Interesse")
plt.show()


## #####################################################
## Teil 6: Ergebnisse der verhergesehenden Daten plotten
## #####################################################

import matplotlib.pyplot as plt

plt.scatter(X_test[:, 0], X_test[:, 1], c=y_predicted)
plt.xlabel("Alter")
plt.ylabel("Interesse")
plt.show()

