# note: twitter API has a limit on requests sent not sure exactly what but 2500 requests in <15 minutes breaks it
#import api key from other file
import apikey
from apikey import *

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

auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(auth)

#Sentiment Analysis
def percentage(part,whole):
    return 100 * float(part)/float(whole) 

noOfTweet = int(input ("Please enter how many tweets to analyze: "))

#lastTweetId = 11/20/21
#add since_id = lastTweetId in parameter if want to do specific date to recent 

tweets = tweepy.Cursor(api.search_tweets, q='vaccine -filter:retweets -filter:replies -filter:links', lang="en", tweet_mode = 'extended').items(noOfTweet)
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

    
    print('Username: ', tweet.user.screen_name)
    print('Tweet: ',tweet.text)
    print('Score: ', score)
    
    if neg > pos:
        negative_list.append(tweet.text)
        negative += 1
        print('Classification: negative')

    elif pos > neg:
        positive_list.append(tweet.text)
        positive += 1
        print('Classification: positive')
    
    elif pos == neg:
        neutral_list.append(tweet.text)
        neutral += 1
        print('Classification: neutral')
    
    print('\n')
    print('-----------------------------')    


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