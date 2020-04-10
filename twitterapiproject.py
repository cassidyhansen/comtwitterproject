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
    
#converting data to a Pandas friendly format
import pandas as pd
byu_df = pd.read_json (r'C:\Users\Chase\Desktop\Coding\twitter-cdsw-master\twitter-cdsw-master\byu.json')
export_csv = df.to_csv (r'C:\Users\Chase\Desktop\Coding\twitter-cdsw-master\twitter-cdsw-master\byu.csv', index = None, header=True)

#reading file and getting ready to make a graph
import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv(r'C:\Users\Chase\Desktop\Coding\twitter-cdsw-master\twitter-cdsw-master\byu.csv')

#graphing
df.index = pd.to_datetime(df.created_at) #converting time to analysis friendly format
plt.figure(figsize=(16,5))
plt.xlabel('created_at')

ax1 = df.favorite_count.plot(color='blue', grid=True, label='Favorites')
ax2 = df.retweet_count.plot(color='green', grid=True, secondary_y=True, label='Retweets')

ax1.legend(loc=1)
ax2.legend(loc=2)

plt.show()

#did I repurpose this code? ABSOLUTELY. Shout out to Josh Blum

