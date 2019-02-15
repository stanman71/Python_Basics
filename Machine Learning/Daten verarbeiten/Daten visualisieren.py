

""" Beispiel für die Visualisierung eines Datenpakets """


## ##########################
## Teil 0: Einlesen der Daten
## ##########################

import pandas as pd

df = pd.read_csv("./Python_Training/Machine Learning/Daten verarbeiten/CSV/train.csv.bz2")

X = df.drop("subject", axis = 1).drop("Activity", axis = 1)
y = df["Activity"]


## #######################
## Teil 1: Daten skalieren
## #######################

from sklearn.preprocessing import StandardScaler

s = StandardScaler()
X = s.fit_transform(X)


## ############################
## Teil 2: Daten transformieren
## ############################

from sklearn.decomposition import PCA

p = PCA(n_components = 2)
p.fit(X)

X_transformed = p.transform(X)


## ##########################
## Teil 3: Ergebnisse plotten
## ##########################

import matplotlib.pyplot as plt

plt.figure(figsize = (15, 6))

for activity in y.unique():
    X_transformed_filtered = X_transformed[y == activity, :]
    plt.scatter(X_transformed_filtered[:, 0], X_transformed_filtered[:, 1], label = activity, s = 4)

plt.legend()
plt.show()
