

""" Berechnung wie die Anzahl der Cluster die Qualität der Datenauswertung beeinflusst """


## ##########################
## Teil 0: Einlesen der Daten
## ##########################

import pandas as pd

df = pd.read_csv("./Python_Training/Machine Learning/Clustering/CSV/autos_prepared.csv")

X = df[["yearOfRegistration", "price"]]


## #######################
## Teil 1: Daten skalieren
## #######################

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_transformed = scaler.fit_transform(X)


## ######################
## Teil 2: Cluster bilden
## ######################

from sklearn.cluster import KMeans

scores = []
for n in range(2, 10):
    model = KMeans(n_clusters = n)
    model.fit(X_transformed)
    scores.append(model.inertia_)


## ###########################
## Teil 3: Ergebnisse anzeigen
## ###########################

import matplotlib.pyplot as plt

""" Je niedriger Y, desto besser
    Aber Clusteranzahl nur erhöhen, wenn es mit deutlichen Vorteilen verbunden ist 
    Hier: optimal 3 oder 4"""
plt.plot(range(2, 10), scores)
plt.show()
