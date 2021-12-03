# twitter-sentiment-analysis
## CSE 408 Project - Twitter Sentiment Analysis of Tweets
This project was completed for CSE 408: Multimedia Information Systems at Arizona State University. The purpose of this project explore the accuracy of a sentiment analysis model when performed on tweets which have a 280 character limit.  

The model implemented is developed in Python that performs sentiment analysis using the Natural Language Toolkit on real tweets. We begin by importing our Twitter API keys, the Natural Language Toolkit Sentiment Analysis Analyzer, and several numbers libraries which performs the calculations per tweet.

The the sentiment categorization begins by first defining the list variable “tweets”, which is set equal to the Twitter search API call that searches for the most recent Tweets including the word “vaccine”. The following keyword is used in the search query:
```
q='vaccine -filter:retweets -filter:replies -filter:links'
```  
Adding the filters aims to reduce context ambiguity of replies and duplications of tweets seen in retweets.

Upon collecting the tweets, the full text is then analyzed with the NLTK Sentiment Analysis Analyzer library. This library first preprocesses the text with removing all stop words, generates tokens, and compares the tokens to the pre-defined lexicon from Vader. The score generated returns a positive, neutral, and negative score which add up to 1 and a resulting compound score.

### Results
Upon running two tests of 100 Tweets with the keyword "vaccine", we gathered the following results on Tweet Classifications accuracy:  

True:- Positive: 25, Negative: 67: Neutral: 22  
False:- Positive: 33, Negative 18, Neutral: 34  
  
Average character length length from the sample of 200 tweets: 138.1  

### Discussion
The model implemented in this repository based on our testing data has an average of 57.7% accuracy on tweets. Noted observations during analysis is that shorter Tweets with approximately 10 words or less were defaulted to the neutral classification which impacted the accuracy of the model.

### Dependencies
```
pip install nltk
pip install textblob
pip install tweepy
```
