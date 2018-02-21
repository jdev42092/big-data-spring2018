# Workshop 2: Introduction to Pandas

`Pandas` is a library for Python for data manipulation and analysis. Pandas expands the data processing capacities of Python and adds a number of classes for easily importing data; in particular, it adds numerical tables, from various formats into their DataFrame object. A `DataFrame` is Panda’s basic object that allows multidimensional data processing and indexing. `DataFrames` can be easily and efficiently queried without the need of cumbersome syntax and convoluted loops. `DataFrames` can be merged with other data, they can be sliced, and they can be reshaped. In a way, we can think of Pandas as a combination of Excel and SQL.

## Resources

Pandas's syntax is a bit different from regular Python syntax. However, it is very close to functionality to `NumPy` in that objects are treated as vectors. In this exercise, `NumPy` is generally used for math functions.

You may want to reference a [cheatsheet](https://drive.google.com/folderview?id=0ByIrJAE4KMTtaGhRcXkxNHhmY2M&usp=sharing) to ease the learning curve and learn about some of its functionality:

## Importing the library
First we need to import the libraries we'll be using for this workshop; we'll also use the `as` option to allow us to invoke the library with fewer keystrokes.

```python
import pandas as pd
import numpy as np
```

## Pandas and Data Frames

You can think of a dataframe as a manipulable, multidimensional Python array. They are based on `NumPy` arrays, can hold structured data, and you can perform functions on them to manage data, such as query, select, join, group. Let's set up a really simple dataframe.

```python
# Create empty dataframe
df = pd.DataFrame()

# Create a column
df['name'] = ['Joey', 'Jeremy', 'Jenny']

# View dataframe
df
```

Say we want to add a column. Easy! Use the `assign` method.

```python
# Assign a new column to df called 'age' with a list of ages
df.assign(age = [28, 33, 27])
```

Data in this table can be manipulated, queried, sorted, and munged.

## Reading Files

This is cool and all... but it's the rare situation where you'd actually load data like this. You can imagine how tedious it would get after typing more than a few rows and variables (not to mention all of the windows you're leaving open for human error).

Pandas provides a number of reader functions that process files and return a pandas object or `DataFrame`. Multiple different file types can be read, like `csv`, `txt`, `xls`, and `json`. The `read_table()` function parses the tabular data contained in the files and returns a formatted and indexed `DataFrame`. A number of additional arguments can be specified, allowing us to specify the separator used in delimited text files, which column to use as an index, etc.

Additional documentation can be found on the API:
http://pandas.pydata.org/pandas-docs/stable/index.html

To start us off, let's look at some aggregated cell phone GPS data from a location services company called Skyhook. This is a Boston extract of Skyhook's OpenTide product, which aggregates individual GPS pings to 100x100 meter points. If you're interested, I scraped this from a CARTO product showcasing Skyhook's OpenTide data using a simple script that I've included in this week's materials (`scripts/skyhook_scrape.py`).

This data is too big to upload uncompressed to GitHub, so I've included it as a ZIP file. Extract this zip file and make sure the resulting file is named `skyhook_2017-07.csv`, located in your `week-03` data folder. We then read in the CSV using the pandas `read_csv` function and store it in a new Pandas DataFrame that we call `df` (we could, of course, call it anything).

```python
# If you started Atom from a directory other than the /week-03 directory, you'll need to change Python's working directory. Uncomment these lines and specify your week-03 path.
# import os
# os.chdir('week-03')

# Reading a CSV with Skyhook data
df = pd.read_csv('data/skyhook_2017-07.csv', sep=',')

# We can print the first 5 rows of the dataframe
df.head()
```

Notice we have a table! A spreadsheet! And it indexed the rows. Pandas (borrowing from R) calls it a DataFrame. Lets see the types of the columns.

`df`, in Python context, is an instance of the `pd.DataFrame` class, created by calling the `pd.read_table` function, which calls the DataFrame constructor inside of it. `df` is a dataframe object.

## DataFrame Methods

The df object, for example, has methods, or functions belonging to it, which allow it to do things. For example `df.head()` is a method that shows the first 5 rows of the dataframe. `df.dtypes` returns the data types of each of the columns.

Additional documentation can be found here: http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.html
In general, the API is the best resource: http://pandas.pydata.org/pandas-docs/stable/api.html


```python
df.dtypes
```

We can determine the shape (i.e., the dimensions) of our DataFrame by accessing its `shape` property.

```python
df.shape
```

1,352,529 rows times 10 columns! Not *huge* data by contemporary standards, but definitely big. `df.shape` returns a `tuple`, so we can access members of this `tuple` like we do with a `list`:

```python
# Number of rows
df.shape[0]
# Number of columns
df.shape[1]
```

Let's retrieve the DataFrame's column names. We do this by accessing its columns property. While we're at it, let's look into the data type of the object returned by `df.columns`.

```python
df.columns
type(df.columns)
```

The `df.columns` returns an `Index` object, which is a series. This object is built on top of Python `lists`, and has similar methods and attributes.

We can access an individual column using a simple syntax:

```python
df.cat_name
```

Let's try accessing the `count` column using the same syntax:

```python
df.count
```

Hold the phone... that gave us something quite different. This is because `count` refers to a specific Pandas function that counts the number of non-null observations over a given axis (which in this case didn't work because we didn't specify an axis). To retrieve this column, we can use a more explicit syntax that can't be so easily misinterpreted:

```python
df['count']
```

We can use the `unique()` method to find the unique values in each column. Let's find the unique values in the `cat_name` column.

```python
df.lat.unique()
```

Now lets get multiple columns:

```python
df_multipleColumns = df[['hour', 'cat', 'count']]
df_multipleColumns.head()
```

## Querying

Pandas `DataFrames` have built-in methods for performing queries using a style similar to SQL. This allows us to slice and dice our dataframes with ease. We can apply queries to parts of the `df`, and based on this query select subsets of the whole `df`. Let's do some filtering and querying.

The output of this is a series containing the truth of falsehood of our query - we call this a **mask**.

```python
df['hour'] == 158
```

To print out the table with only the rows we want, we can apply what is called a filter. Our query above returned a **mask**---again, a series containing the Boolean result of evaluating each value in our column against a specified criteria. Let's take a look at a specific time. We can use the `df` mask to get a filtered DataFrame: we use the mask to "index" into the DataFrame to get the rows we want.

```python

time = df[df['hour'] == 158]
time.head
time.shape
```

We see that we now have a DataFrame containing observations in a single hour, subsetted from our DataFrame containing data for all of July 2017. Using `.shape`, we can see that it contains 12,546 rows.

We can query based on multiple criteria using boolean operators (`&` for `and`, `|` for `or`). All we need to do is add `()` brackets around each condition. The query uses a boolean AND. Each condition creates a mask containing `True` and `False` values.

```python
df[(df['hour'] == 158) & (df['count'] > 50)]
```

We've now filtered our dataset substantially: we've limited our results to a single hour and limited our returned cells to those with more than 50 aggregated GPS pings.

Because this dataset contains every day between July 1 and July 31, we can specify a single day that is of interest to us. The fourth of July might seem the obvious choice, but let's imagine we're Francophiles: Bastille day it is.

```python
bastille = df[df['date'] == '2017-07-14']
bastille.head
```

Now that we're celebrating the abolition of French feudalism, we can see which aggregated cells saw greater than average levels of activity:

```python
bastille_enthusiasts = bastille[bastille['count'] > bastille['count'].mean()]
bastille_enthusiasts.head
```

Pandas gives us a simple way to generate summary statistics. The `.describe()` method can be used to return a table that includes the count of non-null rows, their mean, standard deviation, etc.

```python
bastille_enthusiasts['count'].describe()
```

Say that we want to generate summary statistics for each day in the month of July. We can use the `.groupby()` method to collapse a DataFrame on the values stored in a given column. For those of you who know SQL, this should be somewhat familiar; for each unique value stored in the date column, we're executing a given method, in this case, `.describe()`. The output of this operation is a table in which each row represents a date, and each column is a summary statistic of the `count` column.

```python
df.groupby('date')['count'].describe()
```

We can group by multiple columns as well. Let's calculate summary statistics for the `count` column for each hour of each day!

```python
df.groupby(['date', 'hour'])['count'].describe()
```

We can also use built-in pandas methods to calculate individual summary statistics---for example, `.max()`, `.min()`, and `.mean()`!

```python
df['count'].max()
df['count'].min()
df['count'].mean()
df['count'].std()
df['count'].count()
```

You can save these as variables and cast them to strings.

```python
# create min, max, and mean
max_count = df['count'].max()
min_count = df['count'].min()
mean_count = df['count'].mean()

# print out some results
print(f"Maximum number of GPS pings: {max_count}")
print(f"Minimum number of GPS pings: {min_count}")
print(f"Average number of GPS pings: {mean_count}")
```

This isn't necessarily all that useful, though. We're also interested in returning all of the other columns associated with those minimum and maximum values. We can do that like so:

```python
df[df['count'] == df['count'].max()]
```

There is a single row that contains the maximum value of GPS pings. This is not the case for the minimum---the following query returns a table with a large number of rows with only a single GPS ping.

```python
df[df['count'] == df['count'].min()]
```

#### Exercise

Calculate the minimum value and maximum value of the `count` column to find the `hour` with the highest and lowest numbers of GPS pings. You'll want to group by hour.

```python

```

#### Exercise:
Get the average number of GPS pings per hour across the whole dataset.

```python

```

## Cleaning

One of the most common tasks while working with big data is data cleaning. Datasets will be inherently heterogeneous and unstructured. The lack of structure can cause functions to throw errors. We can clean data sets through various methods; if the discrepancies follow a structured pattern, it is possible to use built-in functions, or write our own functions. However, if the errors cannot be structured, we might have to do it manually!

You may have noticed something strange about the `hours` column in this dataset---we are reasonably sure that there are only 24 hours in a day, but the `hours` column ranges from 0-167. This is because the data for each day is not terribly tidy; each day includes a small number of observations from the surrounding week. Further complicating the matter, the 168 hours take place over a week that runs from Sunday to Monday. Finally, the hours of the week are recorded in Greenwich Mean Time, which means that, while we might expect that Sunday corresponds to hours 0-23, Monday corresponds to hours 24-47 etc., it's slightly more complicated: Sunday runs from 163 - 18, spanning the beginning and end of the `hours` column.

We can visualize this problem by making some simple line graphs of our `count` column.

```python
# This line lets us plot in Atom
import matplotlib
# This line allows the results of plots to be displayed inline with our code.
%matplotlib inline

day_hours = df[df['date'] == '2017-07-02'].groupby('hour')['count'].sum()
day_hours.plot()
```

Let's clean the data so that each day contains only those observations that occur during the appropriate day. To do so, we need to first identify which day of the week each calendar day corresponds with. We'll need to convert our `date` column to a `datetime` type that Python can interpret using the Pandas `pd.to_datetime()` function. We do this as follows:

```python
df['date_new'] = pd.to_datetime(df['date'], format='%Y-%m-%d')
```

What we're doing here is creating a new `date_new` column based on our `date` column using the `.to_datetime()` method. We specify a format that our date is stored in. `%Y-%m-%d` means: year with a century month as a decimal number, and day as a decimal number all separated by hyphens. We can confirm that this is correct by looking at several rows of the DataFrame.

```python
df['date'].head
```

Once we've created a new column, we can create another column which uses an internal calendar to determine which day a given calendar date lands on. The one quirk here is that, by convention, the `weekday` function returns a numeric value according to a week that runs from 0 to 6 where 0 is Monday. Our 0 hour is midnight on Sunday, so we'll need to make our weekday number match our `hours` column. We do this using the `.apply() method`.

```python
df['weekday'] = df['date_new'].apply(lambda x: x.weekday() + 1)
df['weekday'].replace(7, 0, inplace = True)
```

`lambda` sounds complicated, but really isn't. It allows us to define a function on the fly---here we're saying "do the following for every row: identify a weekday and add one to the returned value." This results in a range from 1-7 and we still want it to range from 0 to 6, so we replace 7 with 0 using the built-in Pandas `.replace` method.

With this new column, we have everything we need to drop rows that are outside a desired 24-hour time window using a relatively simple for loop:

```python
# df[df['date'] == '2017-07-10'].groupby('hour')['count'].sum()
for i in range(0, 168, 24):
  j = range(0,168,1)[i - 5]
  if (j > i):
    df.drop(df[
    (df['weekday'] == (i/24)) &
    (
    ( (df['hour'] < j) & (df['hour'] > i + 18) ) |
    ( (df['hour'] > i + 18 ) & (df['hour'] < j) )
    )
    ].index, inplace = True)
  else:
    df.drop(df[
    (df['weekday'] == (i/24)) &
    (
    (df['hour'] < j) | (df['hour'] > i + 18 )
    )
    ].index, inplace = True)
```

This looks complicated, but let's break it down. We're running a loop which iterates over a range from 0 to 168, exclusive, using steps of 24. In other words, we're iterating over a week's worth of hours, day-by-day.

But there's a trick. It turns out that these times are logged using Greenwich Mean Time, meaning that Boston is 5 hours behind. This poses a problem when we're dealing with the first day of the week: there are five hours that wrap around the break in the array, occupying elements 163 - 167. If we simply subtract from our `i` value, we'll get negative values; the `hours` column contains no negative values. We therefore create a second range from 0-168 with one-step intervals, which permits us to use those negative numbers to access later elements in the `range`.

We then use a branch to test whether a given day causes the problem of being split over the beginning and end of the range of hours. If our `j` value is greater than our `i` value, we know we have to specify different conditions.

We then use the `.drop()` method to drop rows according to a criteria. We're dropping a row if it's `weekday` is a given value, and its `hour` value is either less than or greater than the window of hours over which that day spans.

Let's see what our dataset looks like after we've performed this cleaning operation:

```python
df.shape
```

We lost a some rows (on the order of 50,000), but we're still left with 1,320,179... not too shabby!

## Exporting Data

Let's export our cleaned data file to a CSV! Easy.

```python
# If you started Atom from a directory other than the /week-03 directory, you may need to change Python's working directory. Uncomment these lines and specify your week-03 path.
# import os
# os.chdir('week-03')
df.to_csv('week-03/data/skyhook_cleaned.csv')
```
