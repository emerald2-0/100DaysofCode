#This script will enable us access all our latest tweets.
import tweepy

#Create a twitter developer account first.

key = '' #api key -- Find them at your app > Keys and Token 
secret = '' #api secret -- Find them at your app > Keys and Token
access_token = '' #access token 
access_secret = ''#access secret

auth = tweepy.OAuthHandler(key, secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

my_tweets = api.user_timeline()
for tweet in my_tweets:
    print(tweet.text)
