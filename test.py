import tweepy

#twitter authentication
consumerKey = "Vso4pXzrTWwxllELi0TNyFl9C"
consumerSecret = "N7UdKUStEG0URQm2LkapdVewNdwuEhAwbyqFxFz986Qy9XyQTI"
accessToken = "1459733764402122755-BlMhCdaq1hCW2vcdc1ymbZCSexkPvy"
accessTokenSecret = "yZ2SaqL3hellFxYnZzQ3S6nMmwap0ohDWrwIjcECJkD31"
auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(auth)

keyword = "trump"
noOfTweet = 5
tweets = tweepy.Cursor(api.search_tweets, q=keyword, lang="en").items(noOfTweet)

for tweet in tweets:
    print(tweet.text)
