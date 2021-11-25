# hello team
# this file is the code from the medium article: https://towardsdatascience.com/step-by-step-twitter-sentiment-analysis-in-python-d6f650ade58d
# note: twitter API has a limit on requests sent not sure exactly what but 2500 requests in <15 minutes breaks it

# Import Librariesfrom textblob import TextBlob
from textblob import TextBlob
import sys
import tweepy
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os
import nltk
import pycountry
import re
import string

from wordcloud import WordCloud, STOPWORDS
from PIL import Image
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from langdetect import detect
from nltk.stem import SnowballStemmer
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from sklearn.feature_extraction.text import CountVectorizer

#twitter authentication
consumerKey = "Vso4pXzrTWwxllELi0TNyFl9C"
consumerSecret = "N7UdKUStEG0URQm2LkapdVewNdwuEhAwbyqFxFz986Qy9XyQTI"
accessToken = "1459733764402122755-BlMhCdaq1hCW2vcdc1ymbZCSexkPvy"
accessTokenSecret = "yZ2SaqL3hellFxYnZzQ3S6nMmwap0ohDWrwIjcECJkD31"
auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(auth)

#Sentiment Analysis

def percentage(part,whole):
    return 100 * float(part)/float(whole) 

noOfTweet = int(input ("Please enter how many tweets to analyze: "))

#tweets = tweepy.Cursor(api.search_tweets, q=keyword, lang="en").items(noOfTweet)
tweets = tweepy.Cursor(api.search_tweets, q='vaccine -filter:retweets -filter:replies', lang="en", tweet_mode = 'extended').items(noOfTweet)
# First you get the tweets in a json object
#tweets = [status._json for status in tweepy.Cursor(api.search_tweets, q=keyword, tweet_mode='extended', lang='en').items(noOfTweet)]

# Now you can iterate over 'results' and store the complete message from each tweet.
positive  = 0
negative = 0
neutral = 0
polarity = 0
tweet_list = []
neutral_list = []
negative_list = []
positive_list = []

for tweet in tweets:
    
    #print(tweet.text)
    tweet.text = tweet.full_text
    tweet_list.append(tweet.text)
    analysis = TextBlob(tweet.text)
    score = SentimentIntensityAnalyzer().polarity_scores(tweet.text)
    neg = score['neg']
    neu = score['neu']
    pos = score['pos']
    comp = score['compound']
    polarity += analysis.sentiment.polarity

    print('\n')
    print(tweet.user.screen_name)
    print(tweet.text)
    print('score: ', score)
    
    if neg > pos:
        negative_list.append(tweet.text)
        negative += 1
        print('classification: negative')

    elif pos > neg:
        positive_list.append(tweet.text)
        positive += 1
        print('classification: positive')
    
    elif pos == neg:
        neutral_list.append(tweet.text)
        neutral += 1
        print('classification: nuetral')
    
    print('\n')
    




positive = percentage(positive, noOfTweet)
negative = percentage(negative, noOfTweet)
neutral = percentage(neutral, noOfTweet)
polarity = percentage(polarity, noOfTweet)
positive = format(positive, '.1f')
negative = format(negative, '.1f')
neutral = format(neutral, '.1f')

#Number of Tweets (Total, Positive, Negative, Neutral)
tweet_list = pd.DataFrame(tweet_list)
neutral_list = pd.DataFrame(neutral_list)
negative_list = pd.DataFrame(negative_list)
positive_list = pd.DataFrame(positive_list)
print("total number: ",len(tweet_list))
print("positive number: ",len(positive_list))
print("negative number: ", len(negative_list))
print("neutral number: ",len(neutral_list))