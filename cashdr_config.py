import tweepy
from os import getenv, name
from tweepy import API
from tweepy import Cursor
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.error import TweepError
from tweepy.streaming import StreamListener

TWITTER_ACCESS_TOKEN = getenv('TWITTER_ACCESS_TOKEN')
TWITTER_ACCESS_TOKEN_SECRET = getenv('TWITTER_ACCESS_TOKEN_SECRET')

# The keys for the Twitter app we're using for API requests
# (https://apps.twitter.com/app/13239588). Read from environment variables.
TWITTER_CONSUMER_KEY = getenv('TWITTER_CONSUMER_KEY')
TWITTER_CONSUMER_SECRET = getenv('TWITTER_CONSUMER_SECRET')
CASHTWITTDR_USER_ID = '1287364596572082179'

class MystreamListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()
    
    def on_status(self, tweet):
        print(f"{tweet.user.name} tweeted: {tweet.text}") 
    
    def on_error(self, status):
        print("error detedted!")
        

# Authenticate to Twitter
twitter_auth = OAuthHandler(TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET)
twitter_auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)

# Create API object
api = API(twitter_auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

# Create a tweet
try:
    print("Authentication OK")
    api.verify_credentials()
except:
    print("Error during authentication")

# api.update_status("What a week in the market!")

timeline = api.home_timeline()
# for tweet in timeline:
    # print(f"{tweet.user.name} said {tweet.text}")

# musk = api.get_user("44196397")
# for tweet in api.search(q="Pi Network", lang="en", rpp=10):
    # print(f"{tweet.user.name}: {tweet.text}")
# tweets_listener = MystreamListener(api)
# stream = Stream(api.auth, tweets_listener)
# stream.filter(track=["Pi", "Bee", "Crypto"], languages="en") 
# 
tweets = api.mentions_timeline()
for tweet in tweets:
    tweet.favorite


        