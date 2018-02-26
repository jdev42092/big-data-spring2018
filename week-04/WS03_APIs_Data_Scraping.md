# Workshop 3: APIs and Data Scraping: Getting Twitter Data

## Set up a Twitter Application

This week we are going to scrape data from the Twitter API and make some plots! We are going to use the Twitter REST API, which lets us query and retrieve samples of Tweets. To do this, you need API keys that are linked to an App that you create through your Twitter account. Your API keys are secret and unique to you and only you, and they gives you access to Twitter data through its API.

### What is an API?

In broad terms, an API is a set of instructions that allow one piece of software to talk to another piece of software; it's a set of instructions for interacting with an application.

Many times, though, when we're interested in data, we mean something slightly more specific. For example, we'll be using the Twitter API, which is designed to let other software send questions to Twitter's database ('how many Tweets contain this keyword?') and retrieve results from those questions. Twitter's instructions for interacting with its various API are [documented here](https://developer.twitter.com/en/docs).

There are a couple of ways to get Twitter data, the REST API is just one of them. The others are to set up a Streamer (which streams real time tweets), or to access the Firehose (this means everything!). Read [this article](https://brightplanet.com/2013/06/twitter-firehose-vs-twitter-api-whats-the-difference-and-why-should-you-care/) for a nice comparison between the methods.

The Twitter REST API is best place to start and what we will use in class. Follow the following steps to get your keys.

* Create a twitter account if you do not already have one.
* Go to [https://apps.twitter.com/](https://apps.twitter.com/) and log in with your twitter credentials.
* Click **"Create New App"** in the upper right corner
* Fill out the form, give it a name like **data_getter_yourname** and a description. The form will ask for a website---good thing we made one of these a few week ago! Use the github.io page you created as the URL. Leave the Callback URL field blank. Agree to the terms and click "Create your Twitter application".
* In the next page, click on **Keys and Access Tokens** tab, and copy your "Consumer Key (API Key)" and "Consumer Key (API Secret)".

## Create a Python script to store your Twitter keys

We need to create a Python file (`.py`) that will contain the Twitter keys. Open Atom, and in the materials for the week, *PASTE* these keys into a new file and save it as `twitter-keys.py`. You need to define two string variables, one for each key. Your code should look like this:

```
# In the file you should define two variables (these must be strings!)
api_key = "your twitter key"
api_secret = "your twitter secret"
```

Using this method, we can then import the keys and use them on a repeated basis, and we can choose not to put this file on Github. Again, make sure your variables store your keys as strings!

## Add to Your .gitignore file

Here's the thing---it's **never** a good idea to include these keys in a publicly accessible script or webpage. This means that these keys should not find their way to GitHub. One way to keep them private is importing the keys as a variable from a separate, untracked file. We can make sure to avoid accidentally pushing the file by adding its name to a `.gitignore` file.

In the root directory of your repo, you should see a file called `.gitignore`. Open this file and take a look. You should see the following line:

```sh
week-04/**/twitter_keys.py
```

This is telling git that it should ignore any changes to files called `twitter_keys.py` in any subdirectory of the week-04 directory. This is a simple way to ensure that we don't inadvertently upload our API keys to the repo. We're safe (so long as your file containing your Twitter keys is called `twitter_keys.py` and is in the week-04 folder or a subdirectory).

## Importing the Libraries and Twitter Keys

We will be using `tweepy`, a Python library that provides wrappers around Twitter's API. Like other Python packages we've used up until this point, we can install `tweepy` from the command line using `pip`. Make sure you're in your virtual environment!

```sh
pip install tweepy
# or, if you have two versions of Python/pip installed:
pip3 install tweepy
```

We'll also be using a JSON parsing package called `jsonpickle`. Install it (`pip install jsonpickle`).

In Atom, make a new .py file where we will be writing our scraper and import the libraries:

```python
import jsonpickle
import tweepy
import pandas as pd

# Imports the keys from the python file
# You may need to change working directory
import os
os.chdir('week-04')
from twitter_keys import api_key, api_secret
```

## Authenticate and Create a Tweepy API Object

Before accessing the Twitter API, we need to submit our credentials; in this case, the required credentials are our API key and our secret API key. Twitter uses something called [OAuth](https://dev.twitter.com/oauth) for API authentication. There are two types of OAuth authentication: *user* and *application*. User authentication is required to post tweets and issue requests on behalf of users. [Application-only authentication](https://dev.twitter.com/oauth/application-only) has higher rate limits but it doesn't allow you to post on a given users' behalf. Because it will allow us to pull more Tweets, we are going to use application authentication.

Tweepy has a built-in function (`AppAuthHandler`) that will pass keys to the API and return authentication information. We can then pass the authentication returned by this function to the `API` function, which creates a `tweepy` API object. This object simplifies the access to the [Twitter API](https://dev.twitter.com/overview/documentation) and provides methods for accessing the API’s endpoints. Thus, authentication and API access using Tweepy looks like this:

```python
auth = tweepy.AppAuthHandler(api_key, api_secret)
# wait_on_rate_limit and wait_on_rate_limit_notify are options that tell our API object to automatically wait before passing additional queries if we come up against Twitter's wait limits (and to inform us when it's doing so).
api = tweepy.API(auth, wait_on_rate_limit = True, wait_on_rate_limit_notify = True)
```

Let's wrap this in a function that will authenticate using a user-provided key and secret key and either return an api object or exit after printing an error if authentication fails. `sys.exit(-1)` is what tells the function to exit if authentication fails.

```python
def auth(key, secret):
  auth = tweepy.AppAuthHandler(key, secret)
  api = tweepy.API(auth, wait_on_rate_limit = True, wait_on_rate_limit_notify = True)
  # Print error and exit if there is an authentication error
  if (not api):
      print ("Can't Authenticate")
      sys.exit(-1)
  else:
      return api
```

We can then call this function as follows:

```python
api = auth(api_key, api_secret)
```

Now we have made a connection with the Twitter API and are ready to write our scraper. For reference, check out the [tweepy documentation](http://docs.tweepy.org/en/v3.5.0/) for a list of all available commands.

## A Quick Word on Endpoints Rate Limits

### Endpoints

We're going to build a function that will use the **GET search/tweets** API endpoint. Basically, an 'endpoint' is a URL that allows requests. An API can maintain many such endpoints, each allowing different queries and returning different data. The **GET search/tweets** endpoint returns a list of Tweets matching the parameters passed by a user. Twitter's [documentation of the GET search/tweets endpoint](https://developer.twitter.com/en/docs/tweets/search/api-reference/get-search-tweets) contains a list of the parameters you can use---it's worth consulting!

### Rate Limits

Twitter places strict limits on how quickly you can download data. A technician would tell you that this is in place to lighten the load on their servers. A political economist would tell you that this is in place to convince you to pay for commercial access.

Either way, we are using the Search API with **Application Access** which limits us as follows: you can query the API at a maximum rate of 450 queries per 15-minute window, each of which returns a maximum of 100 Tweets. This gives us a theoretical maximum of 45,000 Tweets per 15-minute window. Read a bit more about the [Rate Limiting](https://developer.twitter.com/en/docs/basics/rate-limiting) and the specific [rate limits for particular API endpoints](https://developer.twitter.com/en/docs/basics/rate-limits).

If you recall, we set up our API object to automatically adjust for these limits (`api = tweepy.API(auth, wait_on_rate_limit = True, wait_on_rate_limit_notify = True)`), so we should be safe. Other Python wrappers for the Twitter API don't do this---it's one of the reasons that `tweepy` is great!

## Building Our Scraper

Let's build a function to download Tweets. To give credit where credit is due, this code is a modified version of that developed by [Bhaskar Karambelkar](https://www.karambelkar.info/2015/01/how-to-use-twitters-search-rest-api-most-effectively./).

The basic logic is this; Twitter's REST API presents a slight difficulty (as do all REST APIs) because it doesn't maintain state information between queries; it doesn't know at what point the previous query stopped. We get around this by using a variable `max_id` that places an upper limit on the returned Tweets. At the end of every run through our `while` loop, we redefine `max_id` so that it is equal to `new_tweets[-1].id`; this means that the API will go further back in its history instead of returning the same Tweets we just retrieved.

We also set some variables to store our parameters. First, we specify a location in two parts. We specify a `latlng`, next we specify a `radius` that will serve as a search distance. We then concatenate these two variables, according to the format expected by the API. According to the [GET search/tweets documentation](https://developer.twitter.com/en/docs/tweets/search/api-reference/get-search-tweets):

> The [geocode] parameter value is specified by ” latitude,longitude,radius ”, where radius units must be specified as either ” mi ” (miles) or ” km ” (kilometers)

We also build our function to include a parameter `write`, which, if `True`, instructs our function to write the returned tweets to a `json` file, the location of which is passed through the `file` parameter. Finally, we can specify a t_max, which is the maximum number of tweets the search should return before stopping---this is low at the moment, because we want to be able to test our function, but we can ratchet it up to download (literally) millions of Tweets.

Note that we set a number of default values in our `get_tweets` function, including default values for `tweet_max` and a default value of an empty string for `search_term`. We can adjust these when we call the function after defining it by passing parameters (see the bottom of the below code block).

```python
def get_tweets(
    geo, ## FOR TWITTER: Allows us to specify location using lat/long/radius
    out_file, ## LOCAL: specify outfile name and location
    search_term = '', ## FOR TWITTER: Allows us to input search term (defaults to empty)
    tweet_per_query = 100, ## FOR TWITTER
    tweet_max = 150, ## FOR TWITTER
    since_id = None, ## LOCAL
    max_id = -1, ## FOR TWITTER: Tells twitter which tweet ID to begin querrying from
    write = False ## LOCAL
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

# Set a Lat Lon
latlng = '42.359416,-71.093993' # Eric's office (ish)
# Set a search distance
radius = '1mi'
# See tweepy API reference for format specifications
geocode_query = latlng + ',' + radius
# set output file location
file_name = 'data/tweets.json'
# set threshold number of Tweets. Note that it's possible
# to get more than one
t_max = 200

get_tweets(
  geo = geocode_query,
  tweet_max = t_max,
  write = True,
  out_file = file_name
)
```

This function will run as is, allowing you to download Tweets to a `.json` file---give it a go! Once it's downloaded, we can take a quick look at it using a JSON Viewer. However, we might also want to download it into a more Python-legible format so that we can manipulate it and analyze it.

## Parsing Our Tweets

We are going to create a function to parse the result into a Python `Series` that contains the things that we are interested in. Series are sort of like DataFrames with a single row; this makes sense because we are parsing our returned tweets tweet-by-tweet, meaning that we'll never have more than one tweet at a time hitting our parser. The returned object is a Python Series, which our above function can append to a DataFrame.

```python
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
```

We can now uncomment the lines that read `all_tweets = pd.DataFrame()`, `all_tweets = all_tweets.append(parse_tweet(tweet), ignore_index = True)`, and `return all_tweets` in our `get_tweets` function. These lines...

+ Create an empty `DataFrame` called `all_tweets`.
+ Append the series returned by our `parse_tweet` function to the `all_tweets` `DataFrame`.
+ Return the `all_tweets` function when the function finishes running.

Now we can run the `get_tweets` function using the following statement. Because we're now returning a `DataFrame`, we want to bind the result of this function to a variable like so:

```python
tweets = get_tweets(
  geo = geocode_query,
  tweet_max = t_max,
  write = True,
  out_file = file_name
)

tweets.head()
```

## Reloading Downloaded Data

We're about to start cleaning our data; cleaning is not an exact science, and sometimes we'll want to step back and reload our data. For example, we run an `inplace` operation that modifies our DataFrame, and we do so in a way that we regret (i.e., we delete too many rows). This is why we download the data in addition to loading it into a Python DataFrame.

We can always reload our data by running the below command, where `df` is an arbitrary variable name and `path/example_json.json` is the path to, for example, your Tweets:

```python
df = pd.read_json('data/tweets.json')
```

## Let's Explore the Tweets

Let's look through the DataFrame and peek at the Tweets we just downloaded. First, let's import a couple of additional libraries that will let us interact with our file system use `numpy` and `pandas`, and create plots:

```python
# Import some additional libraries that will allow us to plot and interact with the operating system
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
```

Next, let's explore our data a bit. Frequently, it is very helpful to visually examine your data as you're cleaning to get a sense of what must be done; we'll be doing this with the Tweets we grabbed from Twitter. Building on last week, we can do this in Pandas.

## Clean, Group, and Plot the Dataset

Next let's summarize and group our data, and create some plots.

### Group by User Location

When we say 'location', we're not referring to the Tweet's lat/long; instead, we're referring to the self-reported location provided by a user. 'Self-reported' is a compound word that gives data scientists rashes---it turns out that when you give people the ability to input their own location (or anything else for that matter), you'll almost always get an assortment of mixed conventions, misspellings, and 'creative' responses!

```python
tweets.dtypes
```

```python
tweets['location'].unique()
```

Now let's do some grouping and sorting. We are using Pandas to do our analysis, much like last week.

```python

loc_tweets = tweets[tweets['location'] != '']
count_tweets = loc_tweets.groupby('location')['id'].count()
df_count_tweets = count_tweets.to_frame()
df_count_tweets
df_count_tweets.columns
df_count_tweets.columns = ['count']
df_count_tweets

df_count_tweets.sort_index()
```

Let's create a pie chart of these using matplotlib.

```python
# Create a list of colors (from iWantHue)
colors = ["#697dc6","#5faf4c","#7969de","#b5b246",
          "#cc54bc","#4bad89","#d84577","#4eacd7",
          "#cf4e33","#894ea8","#cf8c42","#d58cc9",
          "#737632","#9f4b75","#c36960"]

# Create a pie chart
plt.pie(df_count_tweets['count'], labels=df_count_tweets.index.get_values(), shadow=False, colors=colors)
plt.axis('equal')
plt.tight_layout()
plt.show()

# View the plot

```

### Scatterplot Geolocated Tweets

Next, let's find how many Tweets are geolocated and plot them on a scatterplot. To do this, we'll need to find the rows where both lat and long have non-`null` values.

```python
# Create a filter from df_tweets filtering only those that have values for lat and lon
tweets_geo = tweets[tweets['lon'].notnull() & tweets['lat'].notnull()]
len(tweets_geo)
len(tweets)
```

```python
# Use a scatter plot to make a quick visualization of the data points
# N.B., WHEN I DID THIS, I ONLY HAD SIX OUT OF ABOUT 100 TWEETS!
plt.scatter(tweets_geo['lon'], tweets_geo['lat'], s = 25)
plt.show()
```

### Clean Locations

You saw above that we had a bunch of locations that were very similar. Here, we could use [`replace`](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.replace.html) to clean up our locations. For example, there are many variations on 'Boston', all of which we might want to replace with a consistent 'Boston, MA'. We can use [`str.contains()`](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.str.contains.html) to create a mask which filters our `tweets` DataFrame according to whether or not it contains the string "Boston". We can save the `location` column of the filtered dataset and `replace` all of those different ways of spelling Boston with a consistent value.

```python
bos_list = tweets[tweets['location'].str.contains("Boston")]['location']
tweets['location'].replace(bos_list, 'Boston, MA', inplace = True)

tweets['location'].unique()
```

To finish cleaning the data, you would want to iteratively follow a similar process until you've cleaned all locations and made them conform to a single convention.

### Clean Duplicates

In addition to cleaning locations, we may also have duplicate tweets; this is because retweets all register as the same Tweet. To see the contents of duplicate Tweets, we can use `duplicated`:

```python
tweets[tweets.duplicated(subset = 'content', keep = False)]
```

We can remove duplicates from our columns using `drop_duplicates`, which has a very similar syntax:

```python
tweets.drop_duplicates(subset = 'content', keep = False, inplace = True)
```

## Exporting your Data to CSV

As we saw at the end of last week's workshop, exporting your dataset to a CSV is easy! You can use `to_csv()`.

```python
tweets.to_csv('twitter_data.csv', sep=',', encoding='utf-8')
```
