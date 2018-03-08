# Problem Set 3: Scraping and Cleaning Twitter Data

Now that you know how to scrape data from Twitter, let's extend the exercise a little so you can show us what you know. You will set up the scraper, clean the resulting data, and visualize it. Make sure you get your own Twitter key (AND make sure that you don't accidentally push it to GitHub); careful with your `.gitignore`.

## Graphic Presentation

Make sure to label all your axes and add legends and units (where appropriate)! Think of these graphs as though they were appearing in a published report for an audience unfamiliar with the data.

## Don't Work on Incomplete Data!

One of the dangers of cleaning data is that you inadvertently delete data that is pertinent to your analysis. If you find yourself getting strange results, you can always run previous portions of your script again to rewind your data. See the section called 'reloading your Tweets in the workshop.

## Deliverables

### Push to GitHub

1. A Python script that contains your scraper code in the provided submission folder. You can copy much of the provided scraper, but you'll have to customize it. This should include the code to generate two scatterplots, and the code you use to clean your datasets.
2. Extra Credit: A Python script that contains the code you used to scrape Wikipedia with the BeautifulSoup library.

### Submit to Stellar

1. Your final CSV files---one with no search term, one with your chosen search term---appropriately cleaned.
2. Extra Credit: A CSV file produced by your BeautifulSoup scraper.

## Instructions

### Step 1

Using the Twitter REST API, collect at least 80,000 tweets. Do not specify a search term. Use a lat/lng of `42.359416,-71.093993` and a radius of `5mi`. Note that this will probably take 20-30 minutes to run.

### Solution

```python
import jsonpickle
import tweepy
import pandas as pd
import requests
import bs4
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline


# Imports twitter keys
import os
os.chdir('week-04')
from twitter_keys import api_key, api_secret

def auth(key, secret):
  auth = tweepy.AppAuthHandler(key, secret)
  api = tweepy.API(auth, wait_on_rate_limit = True, wait_on_rate_limit_notify = True)
  # Print error and exit if there is an authentication error
  if (not api):
      print ("Can't Authenticate")
      sys.exit(-1)
  else:
      return api

api = auth(api_key, api_secret)

def get_tweets(
    geo,
    out_file,
    search_term = '',
    tweet_per_query = 100,
    tweet_max = 150,
    since_id = None,
    max_id = -1,
    write = False
  ):
  tweet_count = 0 ## Counts number of tweets collected
  all_tweets = pd.DataFrame()
  while tweet_count < tweet_max:
    try:
      if (max_id <= 0):
        if (not since_id):
          new_tweets = api.search(
            q = search_term,
            rpp = tweet_per_query,
            geocode = geo
          )
        else:
          new_tweets = api.search(
            q = search_term,
            rpp = tweet_per_query,
            geocode = geo,
            since_id = since_id
          )
      else:
        if (not since_id):
          new_tweets = api.search(
            q = search_term,
            rpp = tweet_per_query,
            geocode = geo,
            max_id = str(max_id - 1)
          )
        else:
          new_tweets = api.search(
            q = search_term,
            rpp = tweet_per_query,
            geocode = geo,
            max_id = str(max_id - 1),
            since_id = since_id
          )
      if (not new_tweets):
        print("No more tweets found")
        break
      for tweet in new_tweets:
        all_tweets = all_tweets.append(parse_tweet(tweet), ignore_index = True)
        if write == True:
            with open(out_file, 'w') as f:
                f.write(jsonpickle.encode(tweet._json, unpicklable=False) + '\n')
      max_id = new_tweets[-1].id
      tweet_count += len(new_tweets)
    except tweepy.TweepError as e:
      # Just exit if any error
      print("Error : " + str(e))
      break
  print (f"Downloaded {tweet_count} tweets.")
  return all_tweets


def parse_tweet(tweet):
  p = pd.Series()
  if tweet.coordinates != None:
    p['lat'] = tweet.coordinates['coordinates'][0]
    p['lon'] = tweet.coordinates['coordinates'][1]
  else:
    p['lat'] = None
    p['lon'] = None
  p['location'] = tweet.user.location
  p['id'] = tweet.id_str
  p['content'] = tweet.text
  p['user'] = tweet.user.screen_name
  p['user_id'] = tweet.user.id_str
  p['time'] = str(tweet.created_at)
  return p


latlng = '42.359416,-71.093993'
radius = '5mi'
geocode_query = latlng + ',' + radius
file_name = 'data/ps_tweets.json'
t_max = 2000

tweets = get_tweets(
  geo = geocode_query,
  tweet_max = t_max,
  write = True,
  out_file = file_name
)

tweets.to_json('data/ps_tweets.json')

df = pd.read_json('data/ps_tweets.json')
df.head()
df.shape
df['lon'].notnull().sum()
```
### Step 2

Clean up the data so that variations of the same user-provided location name are replaced with a single variation. Once you've cleaned up the locations, create a pie chart of user-provided locations. Your pie chart should strive for legibility! Let the [`matplotlib` documentation](https://matplotlib.org/api/_as_gen/matplotlib.axes.Axes.pie.html) be your guide!

### Solution

```python
df['location'].unique()

# Remove duplicated tweets and those without location
df[df.duplicated(subset = 'content', keep = False)]
df.drop_duplicates(subset = 'content', keep = False, inplace = True)

cleaned_tweets = df[df['location'] != ""]
cleaned_tweets.shape[0]
  # Down to 1083 records

cleaned_tweets['location'].value_counts()
# Keep Boston, Cambridge, Somerville
bos_list = cleaned_tweets[cleaned_tweets['location'].str.contains("Boston", case = False)]['location']
cleaned_tweets['location'].replace(bos_list, 'Boston, MA', inplace = True)

cam_list = cleaned_tweets[cleaned_tweets['location'].str.contains("Cambridge", case = False)]['location']
cleaned_tweets['location'].replace(cam_list, 'Cambridge, MA', inplace = True)

som_list = cleaned_tweets[cleaned_tweets['location'].str.contains("Somerville", case = False)]['location']
cleaned_tweets['location'].replace(som_list, 'Somerville, MA', inplace = True)

# Make every other record that refers to Massachusetts into 'Elsewhere in Massachusetts'
massachusetts_list = cleaned_tweets[cleaned_tweets['location'].str.contains("Massachusetts", case = False)]['location']
massachusetts_list
cleaned_tweets['location'].replace(massachusetts_list, 'Elsewhere in MA', inplace = True)
ma_list = cleaned_tweets[cleaned_tweets['location'].str.contains(" MA")]['location']
ma_list = [x for x in ma_list if x not in ['Boston, MA','Cambridge, MA','Somerville, MA']]
ma_list
cleaned_tweets['location'].replace(ma_list, 'Elsewhere in MA', inplace = True)

cleaned_tweets['location'].value_counts()

# Move locations that show up less than 10 times into 'Other'
loc_value_counts = cleaned_tweets['location'].value_counts()
cleaned_tweets['location'].replace(loc_value_counts[loc_value_counts < 10].index,'Other', inplace = True)


# Output pie chart
for_pie = cleaned_tweets['location'].value_counts().to_frame()
for_pie.columns = ['count']

plt.pie(for_pie['count'], labels=for_pie.index.get_values(), shadow=False)
plt.axis('equal')
plt.title("Tweets by self-reported location", loc = 'left')
plt.tight_layout()
plt.show()
```

### Step 3

Create a scatterplot showing all of the tweets are that are geolocated (i.e., include a latitude and longitude).

### Solution
```python

geolocated = df[df['lon'].notnull() & df['lat'].notnull()]
geolocated.shape

plt.scatter(geolocated['lon'], geolocated['lat'], alpha = 0.7, color = 'g')
plt.title('Geolocated tweets')
plt.show()

```

### Step 4

Pick a search term (e.g., "housing", "climate", "flood") and collect tweets containing it. Use the same lat/lon and search radius for Boston as you used above. Depending on the search term, you may find that there are relatively few available tweets.

### Solution
```python
latlng = '42.359416,-71.093993'
radius = '5mi'
geocode_query = latlng + ',' + radius
file_name = 'data/ps_celtics_tweets.json'
t_max = 3000

tweets = get_tweets(
  geo = geocode_query,
  tweet_max = t_max,
  write = True,
  out_file = file_name,
  search_term = 'mit',
)

tweets.to_json('data/ps_mit_tweets.json')

df_mit = pd.read_json('data/ps_mit_tweets.json')

df_mit.head()
df_mit['lon'].notnull().sum()
```


### Step 5

Clean the search term data as with the previous data.

```python
df_mit['location'].unique()

# Remove duplicated tweets and those without location
df_mit[df_mit.duplicated(subset = 'content', keep = False)]
df_mit.drop_duplicates(subset = 'content', keep = False, inplace = True)
cleaned_mit_tweets = df_mit[df_mit['location'] != ""]
cleaned_mit_tweets.shape[0]
  # Down to 893 records

cleaned_mit_tweets['location'].value_counts()
# Keep Boston, Cambridge, Somerville
def loc_find_and_clean(data, location, clean, casesens = False):
  loc_list = data[data['location'].str.contains(location, case = casesens)]['location']
  #print(loc_list.unique())
  data['location'].replace(loc_list, clean, inplace = True)


loc_find_and_clean(cleaned_mit_tweets,'Boston','Boston, MA')
loc_find_and_clean(cleaned_mit_tweets,' UK','United Kingdom', casesens = True)
loc_find_and_clean(cleaned_mit_tweets,'Cambridge','Cambridge, MA')
loc_find_and_clean(cleaned_mit_tweets,'Somerville','Somerville, MA')
loc_find_and_clean(cleaned_mit_tweets,'Quito','Quito, Ecuador')
loc_find_and_clean(cleaned_mit_tweets,'Ecuador','Ecuador')
loc_find_and_clean(cleaned_mit_tweets,'London','United Kingdom')
loc_find_and_clean(cleaned_mit_tweets,'India','India')
loc_find_and_clean(cleaned_mit_tweets,' NY','New York')

loc_find_and_clean(cleaned_mit_tweets,' New York','New York', casesens = True)



# Make every other record that refers to Massachusetts into 'Elsewhere in Massachusetts'
massachusetts_list = cleaned_mit_tweets[cleaned_mit_tweets['location'].str.contains("Massachusetts", case = False)]['location']
massachusetts_list
cleaned_mit_tweets['location'].replace(massachusetts_list, 'Elsewhere in MA', inplace = True)
ma_list = cleaned_mit_tweets[cleaned_mit_tweets['location'].str.contains(" MA")]['location']
ma_list = [x for x in ma_list if x not in ['Boston, MA','Cambridge, MA']]
ma_list
cleaned_mit_tweets['location'].replace(ma_list, 'Elsewhere in MA', inplace = True)



loc_find_and_clean(cleaned_mit_tweets,' DC','Washington, DC', casesens = True)
loc_find_and_clean(cleaned_mit_tweets,' CA','California', casesens = True)
loc_find_and_clean(cleaned_mit_tweets,'SF','California', casesens = True)
loc_find_and_clean(cleaned_mit_tweets,'LA','California', casesens = True)
cleaned_mit_tweets['location'].value_counts()

# Move locations that show up less than 8 times into 'Other'
loc_value_counts = cleaned_mit_tweets['location'].value_counts()
cleaned_mit_tweets['location'].replace(loc_value_counts[loc_value_counts < 8].index,'Other', inplace = True)
cleaned_mit_tweets['location'].value_counts()
```

### Step 6

Create a scatterplot showing all of the tweets that include your search term that are geolocated (i.e., include a latitude and longitude).

```python

geolocated_mit = df_mit[df_mit['lon'].notnull() & df_mit['lat'].notnull()]
geolocated_mit.shape

plt.scatter(geolocated_mit['lon'], geolocated_mit['lat'], alpha = 0.7, color = 'g')
plt.title('Geolocated tweets about MIT')
plt.show()
```

### Step 7

Export your scraped Twitter datasets (one with a search term, one without) to two CSV files. We will be checking this CSV file for duplicates and for consistent location names, so make sure you clean carefully!

```python
cleaned_tweets.to_csv('data/twitter_data.csv', sep=',', encoding='utf-8')
cleaned_mit_tweets.to_csv('data/twitter_data_about_mit.csv', sep=',', encoding='utf-8')
```

## Extra Credit Opportunity

Build a scraper that downloads and parses the Wikipedia [List of Countries by Greenhouse Gas Emissions page](https://en.wikipedia.org/wiki/List_of_countries_by_greenhouse_gas_emissions) using BeautifulSoup and outputs the table of countries as as a CSV.
