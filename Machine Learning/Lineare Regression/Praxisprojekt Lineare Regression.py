
import pandas as pd

df = pd.read_csv("./Python_Training/Machine Learning/Lineare Regression/CSV/autos_prepared.csv")
df.head()



## Teil 1: Scatter-Plot zeichnen


import matplotlib.pyplot as plt

plt.scatter(df["kilometer"], df["price"])
plt.show()



## Teil 2: Lineare Regression ausführen


from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(df[["kilometer"]], df[["price"]])

print("Intercept: " + str(model.intercept_))
print("Coef: " + str(model.coef_))

# 15988.72674252 - 0.0879714 * [Anzahl km] 



## Teil 3: Werte für unsere Linie vorhersagen


predicted = model.predict([[0], [130000]])
print(predicted)



## Teil 4: Linie in Grafik einzeichnen


import matplotlib.pyplot as plt

plt.scatter(df["kilometer"], df["price"])
plt.plot([0, 130000], predicted, color="red")
plt.show()



## Teil 5: Vorhersage für 50.000km machen


model.predict([[50000]])


