from sklearn.naive_bayes import BernoulliNB
from sklearn import model_selection


def data_generate(data, size, target):
    data_train, data_test, target_train, target_test = model_selection.train_test_split(data, target, test_size=size, random_state=43)
    return data_train, data_test, target_train, target_test


def learn(data, target):
    classifier = BernoulliNB().fit(data, target)
    return classifier


def predict(data, classifier,):
    return classifier.predict(data)