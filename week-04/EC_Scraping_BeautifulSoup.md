# Supplementary Skill: Web Scraping Using Beautiful Soup

Let's scrape some data using a fun library called Beautiful Soup. We'll create a CSV dataset by scraping a table on 311 reported Rodent Incidents around Boston, hosted [here](http://duspviz.mit.edu/_assets/data/sample.html).

Let's get started!

## Importing Modules

First import modules. `import requests` imports the requests module, and `import bs4` imports the Beautiful Soup library.

```python
# You'll probably have to install BeautifulSoup and requests using pip.
import requests
import bs4
```

## Requests

Requests will allow us to load a webpage into python so that we can parse it and manipulate it. Test this by running the following. I am using a really simple page from the Beautiful Soup documentation to explain what is happening here. Enter the following commands in terminal, and hit enter after entering each to run each of them.


```python
response = requests.get('http://duspviz.mit.edu/_assets/data/sample.html')
print(response.text) # Print the output
```

This allowed us to access all of the content from the source code of the webpage with Python, which we can now parse and extract data. It even printed to our console. Pretty cool!

## Beautiful Soup

Beautiful Soup is a Python library for parsing data out of HTML and XML files (for example, webpages). It provides idiomatic ways of navigating, searching, and modifying the parse tree. Beautiful Soup's central functionality is that it allows you to access elements of your page by following paths through a structured document; for example, this will allow you to easily grab all links, all headers, or every instance of a specific class.

Once we've selected elements and structured them, Python makes it easy to write these into portable file formats such as a CSV.

The sample webpage we are using contains data on rodent incidents in the greater Boston area. Let's parse this webpage---which we've downloaded using `requests`---and extract some data.

### Make the Soup

First, we have to turn the website code into a Python object. We have already imported the Beautiful Soup library, so we can start calling some of the methods in the library. The following code turns the text into an Python object named **soup**. The following line uses the Beautiful Soup **prettify()** function, which formats the text contained in the 'soup' in a readable and legible manner.

```python
soup = bs4.BeautifulSoup(response.text, "html.parser")
print(soup.prettify()) # Print the output using the 'prettify' function
```

An important note: You need to specify a parser for Beautiful Soup to parse your text. This is done in the second argument of the BeautifulSoup function; above, we specify 'html.parser'. You an also use **lxml** or **html5lib**. This is described in the [documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-a-parser). For our purposes, 'html.parser' will be fine.

At any point, if you need a reference, visit the [Beautiful Soup documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#) for the official descriptions of functions. Prettify is a handy one to see our document in a clean fashion.

#### Navigating the Data Structure

With our data from the webpage read into the soup, we can now navigate the data structure. We called our Beautiful Soup object **soup**: we can run Beautiful Soup functions on this object. Let's explore some of these; try running the following lines of code.


```python
# Access the title element
soup.title
```


```python
# Access the content of the title element
soup.title.string
```


```python
# Access data in the first 'p' tag
soup.p
```


```python
# Access data in the first 'a' tag
soup.a
```


```python
# Retrieve all links in the document (note it returns an array)
soup.find_all('a')
```


```python
# Retrieve elements by class equal to link using the attributes argument
soup.findAll(attrs={'class' : 'link'})
```


```python
# Retrieve a specific link by ID
soup.find(id="link3")
```


```python
# Access Data in the table (note it returns an array)
soup.find_all('td')
```

#### Working with Arrays

The easiest way to access elements and then either write them to file or manipulate them is to save them as objects. Note that our data is organized into columns storing cities and numbers. Let's save these to arrays.

The following gives us an array which will allow us to work with the elements.

```python
data = soup.findAll(attrs={'class':'city'})
print(data[0].string)
print(data[1].string)
print(data[2].string)
print(data[3].string)
```

You never want to repeat code like this, so turn this into a loop:

```python
data = soup.findAll(attrs={'class':'city'})
for i in data:
    print(i.string)
```

This array only gives us cities though, let's get all of the data elements that have either class `city` or class `number`.

```python
data = soup.findAll(attrs={'class':['city','number']})
print(data)
```

We have all of our data that was nested in these tags saved to a Python array. Access the elements of the array by using `data[x]`, where x is location in the array. In Python, arrays start at 0, so place 1 in a Python array is actually called by using a 0, and place 8 would be called by a 7.

```python
print(data[0])
print(data[1])
```

Right now, we get the whole element with those commands. To get just the content, use the following.


```python
print(data[0].string)
print(data[1].string)
```

In the next part, we'll create a script file and run it!

## Create and execute Script File (`.py`)

Open up `starter_script.py` in Atom; we walk through the code in that file below.

For the first lines in the file, lets import modules. `import requests` imports the requests module, and `import bs4` imports the Beautiful Soup library. We then download the page, turn it into a parseable 'soup', and specify elements of interest. Let's put a print at the end so we can see our work as it runs.

```python
import requests
import bs4

# load and get the website
response = requests.get('http://duspviz.mit.edu/_assets/data/sample.html')

# create the soup
soup = bs4.BeautifulSoup(response.text, "html.parser")

# find all the tags with class city or number
data = soup.findAll(attrs={'class':['city','number']})

# print 'data' to console
print(data)
```

Run this using Hydrogen, or using `python` in the terminal. You should see an array with our data elements nested within tags. Nice!

## Write data to a file using a simple loop

Python makes opening a file and writing to it relatively easy. Let's write our simple dataset to a file in our current working directory.

In pseudo-code, we will:

1. Open up a file to write in and append data.
2. Set up parameters for the while loop
3. Write headers
4. Run while loop that will write elements of the array to file
5. When complete, close the file

Once done, open the file on your machine and see your data. Enter the following code, note what each line is doing.

```python
f = open('rat_data.txt','a') # open new file, make sure path to your data file is correct

p = 0 # initial place in array
l = len(data)-1 # length of array minus one

f.write("City, Number\n") #write headers

while p < l: # while place is less than length
    f.write(data[p].string + ", ") # write city and add comma
    p = p + 1 # increment
    f.write(data[p].string + "\n") # write number and line break
    p = p + 1 # increment

f.close() # close file
```

Save and run the file. You'll see `rat_data.txt` appear in your working folder; when you open this file in Atom, you'll see that it is a simple CSV with the data from the page!

```sh
City, Number
Cambridge, 400
Boston, 900
Somerville, 300
Brookline, 600
```

Further reading on file read/write in Python can be found in the [Python File Reading and Writing Documentation](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)

We created this CSV manually to illustrate some basic Python. Python has modules and features that support CSV as well that are very useful. These are best if you are reading in a CSV, allowing you to access the elements of the CSV. You can read more about the built in CSV module [here](https://docs.python.org/3/library/csv.html).

#### Beautiful Soup Tutorials
http://www.crummy.com/software/BeautifulSoup/bs4/doc/
