# import json
# import time
# import threading
import tweepy
import jsonpickle
# from datetime import datetime
from twitter_keys import api_key, api_secret

def auth(key, secret):
    # Create a Twython object called twitter
    # Set this up using your Twitter Keys, imported from twitter_keys.py
    auth = tweepy.AppAuthHandler(key, secret)
    # Get an OAuth2 access token, save as variable so we can launch our app.
    api = tweepy.API(auth, wait_on_rate_limit = True, wait_on_rate_limit_notify = True)
  # Print error and exit if there is an authentication error
    if (not api):
        print ("Can't Authenticate")
        sys.exit(-1)
    else:
        return api

api = auth(api_key, api_secret)

# Setup a Lat Lon
latlng = '42.359416,-71.093993' # Eric's office (ish)
# Setup a search distance
distance = '1mi'
# See tweepy API reference for format specifications
geocode_query = latlng + ',' + distance
# tweet_max = 1500000000
# tweet_per_query = 100
file_name = 'data/tweets.json'


tweets = get_tweets(tweet_max = 15, geo = geocode_query, write = True)

def get_tweets(geo, search_term = '', tweet_per_query = 100, tweet_max = 150, since_id = None, max_id = -1, write = False):
    tweet_count = 0
    all_tweets = {}
    while tweet_count < tweet_max:
        try:
            if (max_id <= 0):
                if (not since_id):
                  new_tweets = api.search(q = search_term, rpp = tweet_per_query, geocode = geo)
                else:
                  new_tweets = api.search(q = search_term, rpp = tweet_per_query, geocode = geo, since_id = since_id)
            else:
                if (not since_id):
                  new_tweets = api.search(q = search_term, rpp = tweet_per_query, geocode = geo, max_id = str(max_id - 1))
                else:
                  new_tweets = api.search(q = search_term, rpp = tweet_per_query, geocode = geo, max_id = str(max_id - 1), since_id = since_id)
            if (not new_tweets):
                print("No more tweets found")
                break
            for tweet in new_tweets:
                if write == True:
                    with open('data/tweets.json', 'w') as f:
                        f.write(jsonpickle.encode(tweet._json, unpicklable=False) + '\n')
                all_tweets[tweet.id_str] = parse_tweet(tweet)
            max_id = new_tweets[-1].id
            tweet_count += len(new_tweets)
        except tweepy.TweepError as e:
          # Just exit if any error
          print("Error : " + str(e))
          break
    print (f"Downloaded {tweet_count} tweets.")
    return all_tweets

def parse_tweet(tweet):
    properties = {}
    if tweet.coordinates != None:
         properties['lat'] = tweet.coordinates['coordinates'][0]
         properties['lon'] = tweet.coordinates['coordinates'][1]
    else:
         properties['lat'] = None
         properties['lon'] = None
    properties['location'] = tweet.user.location
    properties['id'] = tweet.id_str
    properties['content'] = tweet.text
    properties['user'] = tweet.user.screen_name
    properties['user_id'] = tweet.user.id_str
    # properties['raw_source'] = tweet
    properties['time'] = str(tweet.created_at)
    return properties
