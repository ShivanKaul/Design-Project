import numpy as np
# from sklearn.cross_validation import cross_val_predict
# from sklearn.cross_validation import cross_val_score
from sklearn.cross_validation import train_test_split
# from sklearn import linear_model
from sklearn import svm
from scipy import stats
from scipy.stats import itemfreq

TYPE_INDEX = 3


def learn_with_test(dataset, testset):
    matrix_ds = np.asarray(dataset)
    matrix_ds_test = np.asarray(dataset)
    clf = svm.SVC(kernel='rbf', C=5)
    training_target = matrix_ds[:, TYPE_INDEX]
    training_dataset = matrix_ds[:, 1:TYPE_INDEX].astype(np.float)
    testing_target = matrix_ds_test[:, TYPE_INDEX]
    testing_dataset = matrix_ds_test[:, 1:TYPE_INDEX].astype(np.float)

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
    clf = svm.SVC(kernel='rbf', C=5)
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
