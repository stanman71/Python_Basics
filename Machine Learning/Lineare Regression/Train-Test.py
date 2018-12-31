
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt


df = pd.read_csv("./Python_Training/Machine Learning/Lineare Regression/CSV/wohnungspreise.csv")
df.head()


X = df[["Quadratmeter"]].values
Y = df[["Verkaufspreis"]].values

X_train, X_test, y_train, y_test = train_test_split(X, Y, random_state = 0, test_size = 0.25)


plt.scatter(X_train, y_train)
plt.scatter(X_test, y_test, color = "red")
plt.show()


model = LinearRegression()
model.fit(X_train, y_train)

print("Intercept: " + str(model.intercept_))
print("Coef: " + str(model.coef_))


predicted = model.predict(X_test)

plt.scatter(X_test, y_test, color = "red")
plt.plot(X_test, predicted)
plt.show()


