# Sentiment-analysis-of-streaming-tweets
It is a software built on python 2.7 used for sentiment analysis of streaming tweets.

## Following are the packages required for the software:
```
1. Scikit-learn
2. Tweepy
3. yweather
4. Pickle
```

## How to run the sentiment analysis on streaming tweets?
1. Download 
      * Sentiment140 dataset
        * [Stanford link](http://cs.stanford.edu/people/alecmgo/trainingandtestdata.zip)
2. Extract the downloaded zip file and store the extracted files in the main folder.
3. Create a twitter app [here](https://apps.twitter.com)
4. Follow the tutorial given in the following link for creating and getting tokens and keys.
     * [Connect your app to Twitter](https://auth0.com/docs/connections/social/twitter)
5. Paste the keys and tokens in twitter_streaming.py
6. In shell type "**python main(streaming).py**" without quotes.
7. When it asks for the path of dataset, provide the path of Sentiment140 training dataset.

## How to test your trained model?
1. In shell type "**python test.py**" without quotes.
2. If it asks for the path of dataset, provide the path of Sentiment140 training dataset.
### Happy sentiment analysing!!!
