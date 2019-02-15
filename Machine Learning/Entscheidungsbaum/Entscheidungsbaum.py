

""" Entscheidungsbäume sind geordnete, gerichtete Bäume, die der Darstellung von 
    Entscheidungsregeln dienen. 

    Entropie
    > Maß für den mittleren Informationsgehalt einer Nachricht
    > Im Entscheidungsbaum wie viele Daten noch abweichen (Ziel: 0) """


## ##########################
## Teil 0: Einlesen der Daten
## ##########################

import pandas as pd

df = pd.read_csv("./Python_Training/Machine Learning/Entscheidungsbaum/CSV/classification.csv")


## ################################################################
## Teil 1: Aufteilung in Trainings- und Testdaten (hier: 75% / 25%)
## ################################################################

from sklearn.model_selection import train_test_split

# Welche Spalten sollen zur Vorhersage verwendet werden
X = df[["age", "interest"]].values

""" Oder: Die Spalte "success" soll nicht zur Vorhersage verwendet werden:
    X = df.drop("success", axis = 1).values """

y = df["success"].values

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 0, test_size = 0.25)


## ##########################
## Teil 2: DecisionTree bauen
## ##########################

from sklearn.tree import DecisionTreeClassifier

model = DecisionTreeClassifier(criterion = "entropy", max_depth = 4, min_samples_leaf = 3)
model.fit(X_train, y_train)

print(model.score(X_test, y_test))


## ############################
## Teil 3: DecisionTree plotten
## ############################

""" Hinweis: Benötigt plot_classifier.py """

from plot_classifier import plot_classifier

# Trainings-Daten plotten
plot_classifier(model, X_train, y_train, proba = True, xlabel = "Alter", ylabel = "Interesse")

# Testdaten plotten
plot_classifier(model, X_test, y_test, proba = True, xlabel = "Alter", ylabel = "Interesse")


## ################################
## Teil 4: DecisionTree exportieren
## ################################

from sklearn.tree import export_graphviz
import graphviz
import os

""" Install windows package from:   
    https://graphviz.gitlab.io/_pages/Download/Download_windows.html """

os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'

tree = export_graphviz(model, None, 
                       feature_names = ["age", "interest"], 
                       class_names = ["nicht gekauft", "gekauft"],
                       rounded = True,
                       filled = True)

src = graphviz.Source(tree, format = "png")
src.render("./Python_Training/Machine Learning/Entscheidungsbaum/Export/tree_export")

