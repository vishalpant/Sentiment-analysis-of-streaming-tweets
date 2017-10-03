import csv
import pickle


def load_data(name, delimiter, quotechar, datacolumn, weightcolumn):
    read = open(name)
    reader = csv.reader(read, delimiter=delimiter, quotechar=quotechar)
    reader.next()
    data = []
    target = []
    for row in reader:
        if row[datacolumn] and row[weightcolumn]:
            data.append(row[datacolumn].decode("utf-8", "ignore"))
            target.append(row[weightcolumn])
    return data,target


def load_tweets():
    read = open("tweets.pickle", "rb")
    data = pickle.load(read)
    read.close()
    return data


def load_sentiments():
    read = open("sentiments.pickle", "rb")
    sentiments = pickle.load(read)
    read.close()
    return sentiments


def save_tweets(tweets):
    write_tweets = open("tweets.pickle", "wb")
    pickle.dump(tweets, write_tweets)
    write_tweets.close()


def save_sentiments(sentiments):
    write_sentiments = open("sentiments.pickle", "wb")
    pickle.dump(sentiments, write_sentiments)
    write_sentiments.close()