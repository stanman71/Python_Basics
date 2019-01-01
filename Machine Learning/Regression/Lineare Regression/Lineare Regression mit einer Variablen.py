

## Teil 0: Einlesen der Daten

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("./Python_Training/Machine Learning/Regression/Lineare Regression/CSV/wohnungspreise.csv")
df.head()

plt.scatter(df["Quadratmeter"], df["Verkaufspreis"])
plt.show()



## Teil 1: Berechnung der Funktion

from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(df[["Quadratmeter"]], df[["Verkaufspreis"]])

print("Intercept: " + str(model.intercept_))
print("Coef: " + str(model.coef_))


# Verkaufspreis = 3143.28481869 + 5071.35242619 * Quadratmeter
# y = 3143.28481869 + 5071.35242619 * x

print(3143.28481869 + 5071.35242619 * 40)



## Teil 2: Abbildung der Regressionsgerade

min_x = min(df["Quadratmeter"])  # erster Wert als Startpunkt
max_x = max(df["Quadratmeter"])  # letzter Wert als Endpunkt

predicted = model.predict([[min_x], [max_x]])

plt.scatter(df["Quadratmeter"], df["Verkaufspreis"])
plt.plot([min_x, max_x], predicted, color = "red")
plt.show()


