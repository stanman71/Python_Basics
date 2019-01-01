

###################################
# Dient zur Überprüfung des Modells
###################################


## Teil 0: Einlesen der Daten

import pandas as pd

df = pd.read_csv("./Python_Training/Machine Learning/Regression/Lineare Regression/CSV/wohnungspreise.csv")
df.head()

X = df[["Quadratmeter"]].values
Y = df[["Verkaufspreis"]].values



## Teil 1: Aufteilung in Trainings- und Testdaten (hier: 75% / 25%)

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, Y, random_state = 0, test_size = 0.25)



## Teil 2: Abbildung der unterschiedlichen Verwendungen

import matplotlib.pyplot as plt

plt.scatter(X_train, y_train)
plt.scatter(X_test, y_test, color = "red")
plt.show()



## Teil 2: Model trainieren

from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X_train, y_train)

print("Intercept: " + str(model.intercept_))  # Fixwert a
print("Coef: " + str(model.coef_))            # Steigung x



## Teil 4: Vergleich der berechneten Gerade mit dem Testdaten

import matplotlib.pyplot as plt

predicted = model.predict(X_test)

plt.scatter(X_test, y_test, color = "red")
plt.plot(X_test, predicted)
plt.show()