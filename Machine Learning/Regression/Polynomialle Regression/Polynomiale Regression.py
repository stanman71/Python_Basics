


# Dient als Erweiterungsoption der linearen Regression


## Teil 0: Daten einlesen

import pandas as pd

df = pd.read_csv("./Python_Training/Machine Learning/Regression/Polynomialle Regression/CSV/fields.csv")

df.head()



## Modell 1: Normale, lineare Regression

X = df[["width", "length"]].values
Y = df[["profit"]].values

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, Y, random_state = 42, test_size = 0.25)

from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X_train, y_train)

print(model.score(X_test, y_test))




## Modell 2: Polynomiale Regression (Grad 2)

from sklearn.preprocessing import PolynomialFeatures

pf = PolynomialFeatures(degree = 2, include_bias = False)
pf.fit(X_train)

""" Daten transformieren """
X_train_transformed = pf.transform(X_train)  [:, [0, 2]] # nur bestimmte Spalten berücksichtigen
X_test_transformed  = pf.transform(X_test)   [:, [0, 2]] # hier: Spalte 0 und 2 

""" auf Basis der trasformierten Daten eine lineare Regression durchführen """
from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X_train_transformed, y_train)

print(model.score(X_test_transformed, y_test))

""" Ausgabe der Spaltenmodifikation (Gibt Hochzahl für jeden Eintrag an) """
print(pf.powers_)

