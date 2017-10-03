import Filter
import load
import Sentiment
import os

if __name__ == '__main__':
    if not os.path.isfile("sentiments.pickle") or not os.path.isfile("tweets.pickle"):
        datafile = str(raw_input("Enter path of training data(Should be in .csv)"))
        #replace 4th parameter with the column number of your tweets
        #replace 5th parameter with the column number of your sentiments
        data, target = load.load_data(datafile, ",", '"', 5, 0)
        load.save_sentiments(target)
        load.save_tweets(data)
    else:
        data = load.load_tweets()
        target = load.load_sentiments()
    data.append(str(raw_input("Enter a tweet:")))
    target.append(0)
    tf_idf = Filter.filter(data)
    classifier = Sentiment.learn(tf_idf[:len(data)-2], target[:len(target)-2])
    prediction = Sentiment.predict(tf_idf[len(data)-1], classifier)
    #sentiment greater than 2 is positive, less than 2 is negative and equal to 2 is neutral.
    #Update if have different type
    if int(prediction[0]) > 2:
        print "positive"
    elif int(prediction[0]) < 2:
        print "Negative"
    else:
        print "Neutral"
