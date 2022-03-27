import matplotlib.pyplot as plot
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, plot_confusion_matrix, classification_report, precision_score, recall_score, f1_score, precision_recall_fscore_support, plot_roc_curve


def data_setup():
    x, y = make_classification(n_samples=500, n_features=20, n_classes=2, random_state=0)
    print("Dataset size: ", x.shape, y.shape)
    x_train, x_test, y_train, y_test = train_test_split(
             x, y, random_state=0)
    classifier = SVC(kernel='linear')
    classifier.fit(x_train, y_train)
    y_pred = classifier.predict(x_test)

    return classifier, x_test, y_test, y_pred


def print_accuracy_score(y_test, y_pred):
    accuracy = accuracy_score(y_test, y_pred)

    print("LINEAR MODEL ACCURACY: " + str(accuracy))


def confusion_plot(classifier, x_test, y_test):
    plot_confusion_matrix(classifier, x_test, y_test)
    plot.show()


def print_classification_report(y_test, y_pred):

    print('Precision                                   : %.3f' % precision_score(y_test, y_pred))
    print('Recall                                      : %.3f' % recall_score(y_test, y_pred))
    print('F1-Score                                    : %.3f' % f1_score(y_test, y_pred))
    print('\nPrecision Recall F1-Score Support Per Class : \n', precision_recall_fscore_support(y_test, y_pred))
    print('\nClassification Report                       : ')
    print(classification_report(y_test, y_pred))


def roc_plot(classifier, x_test, y_test):
    plot_roc_curve(classifier, x_test, y_test)
    plot.show()

def main():
    clf, x, y, pred = data_setup()

    #print_accuracy_score(y, pred)
    #confusion_plot(clf, x, y)
    #print_classification_report(y, pred)
    roc_plot(clf, x, y)


if __name__ == "__main__":
    main()
