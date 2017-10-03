from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
import re


def filter_url(data):
    #update it to remove all the links
    return data


def filter(data):
    data = filter_url(data)
    count_vectorizer = CountVectorizer(binary='true')
    newdata = count_vectorizer.fit_transform(data)
    tfidf_data = TfidfTransformer(use_idf=False).fit_transform(newdata)
    return tfidf_data

