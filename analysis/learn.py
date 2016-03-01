import numpy as np
# from sklearn.cross_validation import cross_val_predict
# from sklearn.cross_validation import cross_val_score
from sklearn.cross_validation import train_test_split
from sklearn import linear_model
from sklearn.svm import SVC
from scipy import stats
from scipy.stats import itemfreq
from sklearn.cross_validation import StratifiedShuffleSplit

from sklearn.grid_search import GridSearchCV

TYPE_INDEX = 3
# TYPE_INDEX = 5


def learn_with_test(dataset, testset):
    matrix_ds = np.asarray(dataset)
    matrix_ds_test = np.asarray(testset)
    # clf = linear_model.LogisticRegression()
    training_target = matrix_ds[:, TYPE_INDEX]
    training_dataset = matrix_ds[:, 1:TYPE_INDEX].astype(np.float)
    testing_target = matrix_ds_test[:, TYPE_INDEX]
    testing_dataset = matrix_ds_test[:, 1:TYPE_INDEX].astype(np.float)

    # Parameter selection
    # Set the parameters by cross-validation

    # cv = StratifiedShuffleSplit(training_target, n_iter=5, test_size=0.2, random_state=42)
    # C_range = 10.0 ** np.arange(-3, 3)
    # gamma_range = 10.0 ** np.arange(-3, 3 )
    # param_grid = dict(gamma=gamma_range, C=C_range)

    # clf = GridSearchCV(SVC(), param_grid, cv=cv)
    # clf.fit(training_dataset, training_target)
    # print("The best parameters are %s with a score of %0.2f"
      # % (clf.best_params_, clf.best_score_))
    clf = SVC(kernel='rbf', C=10, gamma=0.1)


    clf.fit(training_dataset, training_target)
    # print clf.score(testing_dataset, testing_target)
    predictions = clf.predict(testing_dataset)
    print itemfreq(predictions)
    # print list(predictions)
    # print clf.score(testing_dataset, testing_target)
    # print  stats.mode(predictions, axis=None)


def learn(dataset):
    # l1 or l2?
    # I want to use logistic regression, with liblinear
    # because I have small dataset
    # http://scikit-learn.org/stable/modules/linear_model.html#logistic-regression

    # target = [item[TYPE_INDEX] for item in dataset]
    # training_data = [item[1:TYPE_INDEX] for item in dataset]

    matrix_ds = np.asarray(dataset)
    # clf = linear_model.LogisticRegression()
    # clf = linear_model.Perceptron()
    clf = SVC(kernel='rbf', C=10, gamma=0.1)
    target = matrix_ds[:, TYPE_INDEX]
    training_data = matrix_ds[:, 1:TYPE_INDEX].astype(np.float)

    # 40% split
    data_train, data_test, target_train, target_test = train_test_split(
                                              training_data,
                                              target,
                                              test_size=0.4,
                                              random_state=0)

    # print target
    # print training_data

    clf.fit(data_train, target_train)
    # scores = cross_val_score(clf, X=data_train, y=target_train)
    # print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))
    # print len(scores)

    # print data_test, target_test
    print clf.score(data_test, target_test)
    # print clf.predict(data_test)

    # training_data = np.array(matrix_ds[:,1:TYPE_INDEX], dtype = 'float_')

    # target = ?
    # predicted = cross_val_predict(lr, dataset, target, cv=10)
