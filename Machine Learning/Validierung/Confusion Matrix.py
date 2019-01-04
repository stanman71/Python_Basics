

""" Die Confusion Matrix zeigt Objekte, die einer falschen Klasse zugeordnet wurden. """


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

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 0, test_size = 0.25)


## #######################
## Teil 2: Model skalieren
## #######################

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
scaler.fit(X_train)

X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)


## ########################
## Teil 3: Model trainieren
## ########################

from sklearn.linear_model import LogisticRegression

model = LogisticRegression(solver='lbfgs')
model.fit(X_train, y_train)

print(model.score(X_test, y_test))


## ##################################
## Teil 4: Confusion Matrix erstellen
## ##################################

""" Format von confusion_matrix:

Modell:                  Nicht wahr    |      Wahr
-----------------------------------------------------------
Realität: Nicht wahr | Richtig negativ | Falsch positiv
Realität: Wahr       | Falsch negativ  | Richtig positiv  """


from sklearn.metrics import confusion_matrix

y_test_pred = model.predict(X_test)

print(confusion_matrix(y_test, y_test_pred))


