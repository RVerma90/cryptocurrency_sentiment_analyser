# Cryptocurrency Sentiment Analysis on Twitter

# Using tweepy and texblob to retrieve recent tweets and analysing sentiment
import tweepy
from textblob import TextBlob

# Authenticate -  Available from twitter
consumer_key = 'jFUxfEJh3ZKuPLoXM3l3UYjfg'
consumer_secret = 'ydbWWN7JdF3PpadwVF1pLkSjwGeMzwrN5E1hnfF9wX0FaWc3tP'

access_token = '299271134-BEPLGXrjYVU0REmK3v1VzCUjtayndToulZLIr92c'
access_token_secret = 'PbzcQ2WanAo8kbpNg5helI9hQ0wlVnk0y7pqif64XcLJt'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# Retrieve Tweets - Search with cryptocurrency
public_tweets = api.search('cryptocurrency')

# Print tweet, polarity (sentiment positive:negative) and subjectivity
for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    print("")
