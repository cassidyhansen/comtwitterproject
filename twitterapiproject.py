#Approximately how many tweets with the keyword "BYU" are beeing retweeted or tweeted?

#twitter API credentials
import tweepy
from twitter_authentication import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api= tweepy.API(auth,wait_on_rate_limit=True)

#code to scrape tweets  based on key words
text_query = ['BYU']

import json
import datetime

result = []

page_ct=0

startSince = '2020-03-09'
endUntil = '2020-03-12'

try:
    for tweet in tweepy.Cursor(api.search, q=text_query, tweet_mode='extended', since=startSince, until=endUntil).items(999999999):
            result.append(tweet._json)

except BaseException as e:
    print('failed on_status,',str(e))

with open('byu.json', 'w') as f:
    json.dump(result,f)
