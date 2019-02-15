

""" Die ROC-Kurve stellt visuell die Abhängigkeit der Effizienz mit der Fehlerrate 
    für verschiedene Parameterwerte dar. """


## ##########################
## Teil 0: Einlesen der Daten
## ##########################

import pandas as pd

df = pd.read_csv("./Python_Training/Machine Learning/Validierung/CSV/classification.csv")


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

model = LogisticRegression(solver="lbfgs")
model.fit(X_train, y_train)

""" vorhergesagte Wahrscheinlichkeiten """
y_test_proba = model.predict_proba(X_test)[:, 1]


## ###########################
## Teil 4: ROC Kurve berechnen
## ###########################

from sklearn.metrics import roc_curve, roc_auc_score
import matplotlib.pyplot as plt

""" fpr = false positive rate, tpr = true positive rate (Confusion Matrix) """
fpr, tpr, thresholds = roc_curve(y_test, y_test_proba)

# Fläche unter der Kurve
print("AUC-Score")
print(roc_auc_score(y_test, y_test_proba))

plt.plot(fpr, tpr)
plt.show()

""" Je größer die Fläche unter der Kurve ist, desto besser das Modell """

