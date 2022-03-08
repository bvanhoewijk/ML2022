#!/usr/bin/env python3

# Copyright (C) 2022 Project Group 127

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License version 3 as
# published by the Free Software Foundation.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

"""
Imports:
"""
import pandas
import sklearn
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from mlxtend.plotting import plot_decision_regions
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier


def decision_tree_classification(train_x, train_y, test_x, test_y):
    tree = DecisionTreeClassifier()
    print("LOADED TREE MODEL")
    tree.fit(train_x, train_y)
    print("FITTED TREE MODEL")
    tree_prediction = tree.predict(test_x)
    print("TESTED TREE MODEL")
    tree_accuracy = accuracy_score(test_y, tree_prediction)
    print("TREE MODEL ACCURACY: " + str(tree_accuracy))
    plot_decision_regions(
        test_x[:500], test_y.astype(np.integer)[:500], clf=tree
    )


def kNN_classification(train_x, train_y, test_x, test_y):
    knn = KNeighborsClassifier(10)
    print("LOADED KNN MODEL")
    knn.fit(train_x, train_y)
    print("FITTED KNN MODEL")
    knn_prediction = knn.predict(test_x)
    print("TESTED KNN MODEL")
    knn_accuracy = accuracy_score(test_y, knn_prediction)
    print("KNN MODEL ACCURACY: " + str(knn_accuracy))
    plot_decision_regions(
        test_x[:500], test_y.astype(np.integer)[:500], clf=knn
    )


def linear_classification(train_x, train_y, test_x, test_y):
    linear = SVC(kernel="linear")
    print("LOADED LINEAR MODEL")
    linear.fit(train_x, train_y)
    print("FITTED LINEAR MODEL")
    linear_prediction = linear.predict(test_x)
    print("TESTED LINEAR MODEL")
    linear_accuracy = accuracy_score(test_y, linear_prediction)
    print("LINEAR MODEL ACCURACY: " + str(linear_accuracy))
    plot_decision_regions(
        test_x[:500], test_y.astype(np.integer)[:500], clf=linear
    )


def load_data():
    training_data = pandas.read_csv("../data/dota2TrainingNamed.csv", sep=",")
    test_data = pandas.read_csv("../data/dota2TestNamed.csv", sep=",")
    training_features_x = training_data.iloc[:, 4:]
    training_class_y = training_data["winning_team"]
    test_features_x = test_data.iloc[:, 4:]
    test_class_y = test_data["winning_team"]
    print("LOADED DATA")
    return training_features_x, training_class_y, test_features_x, test_class_y


def main():
    training_x, training_y, test_x, test_y = load_data()
    linear_classification(training_x, training_y, test_x, test_y)


if __name__ == "__main__":
    main()

"""
Additional information:

"""
