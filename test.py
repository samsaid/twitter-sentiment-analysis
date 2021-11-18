import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import twitter_samples

from nltk.corpus import twitter_samples

pos_tweets = twitter_samples.strings('positive_tweets.json')
neg_tweets = twitter_samples.strings('negative_tweets.json')
text = twitter_samples.strings('tweets.20150430-223406.json')

print(text)
#this would be a document or tweet
neg_sentence = "today SUX!!"
pos_sentence = "im so HAPPY!!!"
sid = SentimentIntensityAnalyzer()
neg_ss = sid.polarity_scores(neg_sentence)
pos_ss = sid.polarity_scores(pos_sentence)

#print('positive sentence score: ', pos_ss)
#print('negative sentence score: ', neg_ss)
