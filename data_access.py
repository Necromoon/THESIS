import tweepy
import configparser
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

config = configparser.ConfigParser()
config.read('config.ini')

api_key = config['twitter']['api_key']
api_key_secret = config['twitter']['api_key_secret']

access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']

auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

keywords = '#DubNation'
limit=100

time= '2022-10-30'

tweets = tweepy.Cursor(api.search_tweets, until=time, result_type='recent', lang='en', q=keywords,
                       count=100, tweet_mode='extended').items(limit)

columns = ['Date', 'User', 'Tweet']
data = []

for tweet in tweets:
    data.append([tweet.created_at, tweet.user.screen_name, tweet.full_text])
    

df = pd.DataFrame(data, columns=columns)

print(df)

df.to_json('test.json')