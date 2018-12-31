

# Abbild der Einträge


import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("./Python_Training/Machine Learning/Lineare Regression/CSV/wohnungspreise.csv")
df.head()

plt.scatter(df["Quadratmeter"], df["Verkaufspreis"])
plt.show()



# Abbild der Regressionsgerade


from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(df[["Quadratmeter"]], df[["Verkaufspreis"]])

print("Intercept: " + str(model.intercept_))
print("Coef: " + str(model.coef_))


# Verkaufspreis = 3143.28481869 + 5071.35242619 * Quadratmeter
# y = 3143.28481869 + 5071.35242619 * x

print(3143.28481869 + 5071.35242619 * 40)


min_x = min(df["Quadratmeter"])
max_x = max(df["Quadratmeter"])

predicted = model.predict([[min_x], [max_x]])

plt.scatter(df["Quadratmeter"], df["Verkaufspreis"])
plt.plot([min_x, max_x], predicted, color = "red")
plt.show()


