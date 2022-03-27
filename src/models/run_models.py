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
import numpy
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import classification_report
from sklearn.metrics import (
    plot_confusion_matrix,
    classification_report,
    precision_score,
    recall_score,
    f1_score,
    precision_recall_fscore_support,
    plot_roc_curve,
)


def random_forest_classification(x_train, y_train, x_val, y_val):
    # Number of trees in random forest
    n_estimators = [int(x) for x in numpy.linspace(start=50, stop=55, num=6)]
    # Number of features to consider at every split
    max_features = ["auto", "sqrt"]
    # Maximum number of levels in tree
    max_depth = [2, 4]
    # Minimum number of samples required to split a node
    min_samples_split = [2, 5]
    # Minimum number of samples required at each leaf node
    min_samples_leaf = [1, 2]
    # Method of selecting samples for training each tree
    bootstrap = [True, False]
    # Create the param grid
    param_grid = {
        "n_estimators": n_estimators,
        "max_features": max_features,
        "max_depth": max_depth,
        "min_samples_split": min_samples_split,
        "min_samples_leaf": min_samples_leaf,
        "bootstrap": bootstrap,
    }
    random_forest = RandomForestClassifier()
    # Default value for cv is 5 for a 5-fold cross validation but I have played
    # around with a few other integers and have found 30 to be a nice balance
    # of computational power and results. Changing the value for verbose just
    # shows more messages regarding the computation time of the fold and how
    # each parameter gets decided.
    grid_random_forest = GridSearchCV(
        estimator=random_forest,
        param_grid=param_grid,
        cv=30,
        verbose=3,
        n_jobs=1,
    )
    grid_random_forest.fit(x_train, y_train)
    print("Best parameters set found on training set:")
    print()
    print(grid_random_forest.best_params_)
    print()
    print("Grid scores on training set:")
    print()
    means = grid_random_forest.cv_results_["mean_test_score"]
    for mean, params in zip(means, grid_random_forest.cv_results_["params"]):
        print("%0.3f for %r" % (mean, params))
    print("Detailed classification report:")
    print()
    y_true, y_pred = y_val, grid_random_forest.predict(x_val)
    print(classification_report(y_true, y_pred))
    print()
    return grid_random_forest


def decision_tree_classification(x_train, y_train, x_val, y_val):
    decision_tree = DecisionTreeClassifier()
    param_grid = {
        "criterion": ["gini", "entropy"],
        "splitter": ["best", "random"],
    }

    grid_decision_tree = GridSearchCV(
        decision_tree, param_grid, scoring="accuracy"
    )
    grid_decision_tree.fit(x_train, y_train)
    print("Best parameters set found on training set:")
    print()
    print(grid_decision_tree.best_params_)
    print()
    print("Grid scores on training set:")
    print()
    means = grid_decision_tree.cv_results_["mean_test_score"]
    for mean, params in zip(means, grid_decision_tree.cv_results_["params"]):
        print("%0.3f for %r" % (mean, params))
    print("Detailed classification report:")
    print()
    y_true, y_pred = y_val, grid_decision_tree.predict(x_val)
    print(classification_report(y_true, y_pred))
    print()
    return grid_decision_tree


def kNN_classification(x_train, y_train, x_val, y_val):
    knn = KNeighborsClassifier()
    k_range = list(range(1, 101))
    param_grid = dict(n_neighbors=k_range)
    grid_knn = GridSearchCV(knn, param_grid, scoring="accuracy")
    grid_knn.fit(x_train, y_train)
    print("Best parameters set found on training set:")
    print()
    print(grid_knn.best_params_)
    print()
    print("Grid scores on training set:")
    print()
    means = grid_knn.cv_results_["mean_test_score"]
    for mean, params in zip(means, grid_knn.cv_results_["params"]):
        print("%0.3f for %r" % (mean, params))
    print("Detailed classification report:")
    print()
    y_true, y_pred = y_val, grid_knn.predict(x_val)
    print(classification_report(y_true, y_pred))
    print()
    return grid_knn


def linear_classification(x_train, y_train, x_val, y_val):
    param_grid = {
        "kernel": ["linear"],
        "C": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100, 1000],
    }
    grid_linear = GridSearchCV(SVC(), param_grid, scoring="accuracy")
    grid_linear.fit(x_train, y_train)
    print("Best parameters set found on training set:")
    print()
    print(grid_linear.best_params_)
    print()
    print("Grid scores on training set:")
    print()
    means = grid_linear.cv_results_["mean_test_score"]
    for mean, params in zip(means, grid_linear.cv_results_["params"]):
        print("%0.3f for %r" % (mean, params))
    print("Detailed classification report:")
    print()
    y_true, y_pred = y_val, grid_linear.predict(x_val)
    print(classification_report(y_true, y_pred))
    print()
    return grid_linear


def load_data():
    api_data = pandas.read_csv(
        "../../data/API/api_dataset_professional_games_better.csv", sep=","
    )
    x = api_data.iloc[:, 2:]
    y = api_data["match_result"]
    x_train_temp, x_test, y_train_temp, y_test = train_test_split(
        x, y, test_size=2000
    )
    x_train, x_val, y_train, y_val = train_test_split(
        x_train_temp, y_train_temp, test_size=2000
    )
    return x_test, y_test, x_val, y_val, x_train, y_train


def plot_accuracy_score(target_y, prediction):
    accuracy = accuracy_score(target_y, prediction)
    print("LINEAR MODEL ACCURACY: " + str(accuracy))


def plot_confusion_matrix(classifier, test_x, test_y):
    plt_confusion_matrix(classifier, test_x, test_y)
    plt.show()


def main():
    x_test, y_test, x_val, y_val, x_train, y_train = load_data()
    linear_model = linear_classification(x_train, y_train, x_val, y_val)
    kNN_model = kNN_classification(x_train, y_train, x_val, y_val)
    decision_tree_model = decision_tree_classification(
        x_train, y_train, x_val, y_val
    )
    random_forest_model = random_forest_classification(
        x_train, y_train, x_val, y_val
    )
    # plot_accuracy_score(test_y, prediction_linear)
    # plot_confusion_matrix(linear_model, x_test, y_test)


if __name__ == "__main__":
    main()

"""
Additional information:

"""
