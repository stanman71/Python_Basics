

""" Auswertung von unbeschrifteten Daten und Zuordnung zu Clustern """


## ##########################
## Teil 0: Einlesen der Daten
## ##########################

import pandas as pd

df = pd.read_csv("./Python_Training/Machine Learning/Clustering/CSV/autos_prepared.csv")


## #############################
## Teil 1: Datenbestand anzeigen
## #############################

import matplotlib.pyplot as plt

plt.scatter(df["yearOfRegistration"], df["price"])
plt.show()

X = df[["yearOfRegistration", "price"]]


## #######################
## Teil 2: Daten skalieren
## #######################

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_transformed = scaler.fit_transform(X)


## ######################
## Teil 3: Cluster bilden
## ######################

from sklearn.cluster import KMeans

model = KMeans(n_clusters = 3)
model.fit(X_transformed)

labels = model.labels_
centers = model.cluster_centers_

centers_transformed = scaler.inverse_transform(centers)


## ###########################
## Teil 4: Ergebnisse anzeigen
## ###########################

import matplotlib.pyplot as plt

""" alpha = Punkte transperent, s = Punkte kleiner """
plt.scatter(df["yearOfRegistration"], df["price"], c = labels, alpha = 0.4, s = 10)

plt.scatter(
    centers_transformed[:, 0], 
    centers_transformed[:, 1], 
    c = range(len(centers_transformed)), 
    marker = "X", 
    s = 150)

plt.show()

