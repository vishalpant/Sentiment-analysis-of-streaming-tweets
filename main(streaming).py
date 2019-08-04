import Filter
import load
import Sentiment
import os
import twitter_streaming
import get_woeid

if __name__ == '__main__':
    if not os.path.isfile("sentiments.pickle") or not os.path.isfile("tweets.pickle"):
        datafile = str(input("Enter path of training data(Should be in .csv)"))
        #replace 4th parameter with the column number of your tweets
        #replace 5th parameter with the column number of your sentiments
        data, target = load.load_data(datafile, ",", '"', 5, 0)
        load.save_sentiments(target)
        load.save_tweets(data)
    else:
        data = load.load_tweets()
        target = load.load_sentiments()
    country = str(input("Enter your contry name:"))
    try:
        woeid = get_woeid.get_woeid(country)
        trends = twitter_streaming.get_trendy(int(woeid))
        Hashtags = [str(x['name']) for x in trends[0]['trends']]
        print("Trends in your country:")
        Hash_tags = ", ".join(Hashtags)
        print(Hash_tags)
    except Exception as e:
        print("Error getting current trends of your country.\nEncountered an exception while getting the trends in your area.\n\t%s"%e)
    track, number = str(input("Enter track and number of tweets(use \",\" as delimiter):")).split(",")
    tweets, sentiments = twitter_streaming.get_data(track, int(number))
    data = data + tweets
    target = target + sentiments
    tf_idf = Filter.filter(data)
    classifier = Sentiment.learn(tf_idf[:1600000], target[:1600000])
    prediction = Sentiment.predict(tf_idf[1599999:], classifier)
    prediction = [int(x) for x in prediction]
    print("\nTotal tweets analyzed: %d"%len(prediction))
    total_positive = 0
    total_negative = 0
    for i in prediction:
        if int(i) == 0:
            total_negative+=1
        else:
            total_positive+=1
    print("Positive : %.2f%c"%(total_positive/(float)(len(prediction))*100, '%'))
    print("Negative : %.2f%c"%(total_negative/(float)(len(prediction))*100, '%'))