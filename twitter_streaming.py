from tweepy import OAuthHandler
from tweepy import API
from tweepy import Cursor

#Variables that contains the user credentials to access Twitter API
access_token = ""
access_token_secret = ""
consumer_key = ""
consumer_secret = ""


def get_data(track, number=100):
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = API(auth)
    tweets = []
    sentiment = []
    for tweet in Cursor(api.search, q=track, count=20, result_type="recent", include_entities=True, lang="en").items(number):
        print tweet.created_at, tweet.text
        tweets.append(tweet.text)
        sentiment.append(tweet.text)
    return tweets, sentiment


def get_trendy(woeid):
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = API(auth)
    return api.trends_place(woeid)

if __name__ == '__main__':
    track, number = raw_input("Enter track and number of tweets(comma separated)").split(",")
    get_data(str(track), int(number))
