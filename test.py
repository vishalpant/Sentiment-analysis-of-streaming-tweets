import load
import os
import Sentiment
import Filter
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score


def evaluate_model(target_true,target_predicted):
    print classification_report(target_true,target_predicted)
    print "The accuracy score is {:.2%}".format(accuracy_score(target_true,target_predicted))


if __name__ == "__main__":
    if not os.path.isfile("sentiments.pickle") or not os.path.isfile("tweets.pickle"):
        datafile = str(raw_input("Enter path of training data(Should be in .csv)"))
        # replace 4th parameter with the column number of your tweets
        # replace 5th parameter with the column number of your sentiments
        data, target = load.load_data(datafile, ",", '"', 5, 0)
        load.save_sentiments(target)
        load.save_tweets(data)
    else:
        data = load.load_tweets()
        target = load.load_sentiments()
    tf_idf = Filter.filter(data)
    #test data is taken to be 40% of total data and remaining 60% is training data
    data_train, data_test, target_train, target_test = Sentiment.data_generate(tf_idf, 0.4, target)
    classifier = Sentiment.learn(data_train, target_train)
    prediction = Sentiment.predict(data_test, classifier)
    evaluate_model(target_test, prediction)