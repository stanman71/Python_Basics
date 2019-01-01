

## Teil 0: Daten einlesen

import pandas as pd

df = pd.read_csv("./Python_Training/Machine Learning/Regression/Polynomialle Regression/CSV/diamonds.csv")

df.head()

# Für Spalte color (nominale Daten) Ersatzwerte bilden
pd.get_dummies(df, columns = ["color"]).head() 



## Modell 1: Lineare Regression auf Basis des "carat" - Wertes

X = df[["carat"]].values
Y = df[["price"]].values

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size = 0.25)

from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X_train, y_train)

print(model.score(X_test, y_test))



## Modell 2: Lineare Regression auf Basis von Breite, Höhe und Länge

X = df[["x", "y", "z"]].values
Y = df[["price"]].values

from sklearn.model_selection import train_test_split

""" zufällige Splittung > Ergebnis fällt bei kleinen Datenbeständen unterschiedlich aus """
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size = 0.25)

from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X_train, y_train)

print(model.score(X_test, y_test))



## Modell 3: Polynomiale Regression, mit Grad 2

from sklearn.linear_model import LinearRegression

X = df[["x", "y", "z"]].values
Y = df[["price"]].values

from sklearn.model_selection import train_test_split

""" zufällige Splittung > Ergebnis fällt bei kleinen Datenbeständen unterschiedlich aus """
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size = 0.25)

from sklearn.preprocessing import PolynomialFeatures

pf = PolynomialFeatures(degree = 2, include_bias = False)
pf.fit(X_train)

X_train_transformed = pf.transform(X_train)
X_test_transformed = pf.transform(X_test)

model = LinearRegression()
model.fit(X_train_transformed, y_train)

print(model.score(X_test_transformed, y_test))


