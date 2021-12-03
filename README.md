# twitter-sentiment-analysis
## CSE 408 Project
This project was completed for CSE 408: Multimedia. The purpose of this project explore the accuracy of a sentiment analysis model when performed on Tweets.  

The model implemented is developed in Python that performs sentiment analysis using the Natural Language Toolkit on real tweets.

We begin by importing our Twitter API keys,the Natural Language Toolkit Sentiment Analysis Analyzer, and several numbers libraries which performs the calculations per tweet.

The the sentiment categorization begins by first defining the list variable “tweets”, which is set equal to the Twitter search API call that searches for the most recent Tweets including the word “vaccine”. The following keyword is used in the search query:
```
q='vaccine -filter:retweets -filter:replies -filter:links'
```
This query string is added to the Twitter Search API to return X amount of recent tweets, while filting out replies, links, and retweets.  

Upon collecting the tweets, the full text is then analyzed with the NLTK Sentiment Analyzer library. This library first preprocesses the text with removing all stop words, generates tokens, and compares the tokens to the pre-defined lexicon from Vader. The score generated populates a positive, neutral, and negative score adding up to 1 and a compound score.

## Results
Upon running two tests of 100 Tweets with the keyword "vaccine", we gathered the following results on Tweet Classifications accuracy:  

True:- Positive: 25, Negative: 67: Neutral: 22  
False:- Positive: 33, Negative 18, Neutral: 34  
  
Average character length length from the sample of 200 tweets: 138.1  

### Discussion
The model implemented had an average of 57.7% accuracy on Tweets. Noted observations include shorter Tweets with less than 10 words were defaulted to the neutral classification which impacted the accuracy of the model, among other factors.

### Dependencies
```
pip install nltk
pip install textblob
pip install tweepy
```
