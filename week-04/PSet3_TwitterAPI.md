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

Using the Twitter REST API, collect at least 2,000 tweets. Do not specify a search term. Use a lat/lng of `42.359416,-71.093993` and a radius of `5mi`. This will take 1-2 minutes to run.

### Step 2

Clean up the data so that variations of the same user-provided location name are replaced with a single variation. Once you've cleaned up the locations, create a pie chart of user-provided locations. Your pie chart should strive for legibility! Let the [`matplotlib` documentation](https://matplotlib.org/api/_as_gen/matplotlib.axes.Axes.pie.html) be your guide!

### Step 3

Create a scatterplot showing all of the tweets are that are geolocated (i.e., include a latitude and longitude).

### Step 4

Pick a search term (e.g., "housing", "climate", "flood") and collect tweets containing it. Use the same lat/lon and search radius for Boston as you used above. Use a maximum of 2,000 tweets; depending on the search term, you may find that there are fewer than 2,000 tweets available.

### Step 5

Clean the search term data as with the previous data.

### Step 6

Create a scatterplot showing all of the tweets that include your search term that are geolocated (i.e., include a latitude and longitude).

### Step 7

Export your scraped Twitter datasets (one with a search term, one without) to two CSV files. We will be checking this CSV file for duplicates and for consistent location names, so make sure you clean carefully!

## Extra Credit Opportunity

Build a scraper that downloads and parses the Wikipedia [List of Countries by Greenhouse Gas Emissions page](https://en.wikipedia.org/wiki/List_of_countries_by_greenhouse_gas_emissions) using BeautifulSoup and outputs the table of countries as as a CSV.
