

""" Bias-Varianz Dilemma

    - Die Bias (Verzerrung) ist der Fehler ausgehend von falschen Annahmen im Lernalgorithmus. 
      > Eine hohe Verzerrung kann einen Algorithmus dazu veranlassen, sich nicht nicht stark 
        genug an den Daten anzupassen (Underfitting).

    - Die Varianz ist der Fehler ausgehend von der Empfindlichkeit auf kleinere Schwankungen 
      in den Trainingsdaten. 
      > Eine hohe Varianz verursacht eine Überanpassung und es wird sich zu sehr an den Daten
        angepasst (Overfitting). """


## ##########################
## Teil 0: Einlesen der Daten
## ##########################

import pandas as pd

df = pd.read_csv("./Python_Training/Machine Learning/Validierung/CSV/classification.csv")

X = df[["age", "interest"]].values
y = df["success"].values


## ########################
## Teil 2: Model trainieren
## ########################

from sklearn.model_selection import validation_curve
from sklearn.neighbors import KNeighborsClassifier

import numpy as np

""" Anzahl der Nachbarn (n_neighbors in KNeighborsClassifier) """
param_range = np.array([40, 30, 20, 15, 10, 8, 7, 6, 5, 4, 3, 2, 1])

train_scores, test_scores = validation_curve(KNeighborsClassifier(), 
                                             X,
                                             y,
                                             param_name = "n_neighbors",
                                             param_range=param_range)


## ##########################
## Teil 3: Ergebnisse plotten
## ##########################

import matplotlib.pyplot as plt

plt.plot(param_range, np.mean(train_scores, axis = 1))
plt.plot(param_range, np.mean(test_scores, axis = 1))

# Hiermit drehen wir die X-Achse um, sie geht jetzt von 40 bis 1.
plt.xlim(np.max(param_range), 0)

plt.show()

""" Blaue  Linie: Training Score 
    Orange Linie: Test Score 
    
    X = Anzahl Nachbarn
    x = 40 > Underfitting / Bias (zu gringer Abstand Training <> Test)
    x = 15 > Optimal
    x = 1  > Overfitting / Varianz (zu großer Abstand Training <> Test) """
