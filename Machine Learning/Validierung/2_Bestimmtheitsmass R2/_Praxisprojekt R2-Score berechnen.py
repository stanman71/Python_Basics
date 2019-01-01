


## Praxisprojekt: R^2 - Wert berechnen

import pandas as pd

df = pd.read_csv("./Python_Training/Machine Learning/Validierung/2_Bestimmtheitsmass R2/CSV/autos_prepared.csv")



## Teil 1: Train / Test (1 Variable)

from sklearn.model_selection import train_test_split

X = df[["kilometer"]].values
Y = df[["price"]].values

X_train, X_test, y_train, y_test = train_test_split(X, Y, random_state = 0, test_size = 0.25)



## Teil 2: Lineare Regression ausführen

from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X_train, y_train)

print(model.score(X_test, y_test))

# 0 (sehr schlecht) <<<>>> 1 (perfekt)



################################################################################



## Teil 1: Train / Test (2 Variable)

from sklearn.model_selection import train_test_split

X = df[["kilometer", "powerPS"]].values
Y = df[["price"]].values

X_train, X_test, y_train, y_test = train_test_split(X, Y, random_state = 0, test_size = 0.25)



## Teil 2: Lineare Regression ausführen

from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X_train, y_train)
print(model.score(X_test, y_test))

# 0 (sehr schlecht) <<<>>> 1 (perfekt)
