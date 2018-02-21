# Workshop 1: Introduction to Python

## Starting out

### Activate your virtual environment

Recall that last week, we installed the `virtualenv` package using `pip`. Consult those directions again if, for whatever reason, you don't have `virtualenv` installed or you haven't created a `bdvs` virtual environment. To activate our virtual environment, we simply need to run a single command in Terminal or Git Bash:

```sh
. ~/.venvs/bdvs/bin/activate
```

Once you've executed this command, you should see `(bdvs)` at the front of the line in Terminal. This means that you're working in your virtual environment!

### Start Atom from the Terminal

Now that we're within our virtual environment, we need to start Atom from the command line. It's important that you follow this step! Otherwise, Atom and Hydrogen will be working with your system Python installation instead of the environment we're curating.

Change directory to your local clone of the class repo and launch Atom. This can be done like so:

```sh
cd /path/to/local/clone/big-data-spring2018
atom ./
```

When Atom launches, you should see the repo's directory tree on the left side of the screen.

## Todays agenda:

+ What is Python?
+ Python Libraries
+ Python Datatypes and Structures
+ How Python thinks: With objects!
+ Flow Control

## What is Python?

[Python](https://www.python.org/) is a very, very popular high-level programming language. It emphasizes legibility over highly complex structure. Python provides simple data structures that allow for easy data manipulation. Python's simplicity and legibility has led to a large and devoted user community who have created numerous libraries that vastly extend the basic capacities of the language.

Python is an "interpreted" language. This means that every Python command that is executed is actually translated to lower-level programming languages. Lower-level, compiled programming languages (for example, C++) are very fast and powerful, but writing programs in these languages can be difficult.

There are two main versions of Python, these are Python 2 and Python 3. Python 3 is newer, and removed bugs and idiosyncrasies of Python 2; however Python 2 is still heavily used. While the fundamentals of the two versions are the same, there are some differences (mostly syntactical) between the two. These differences are substantial enough that, unfortunately, Python 3 is NOT backwards compatible, so always double check which version of Python a given script is written in. It should be documented, but if it isn't, you can consult a [Python 2 vs. Python 3 cheatsheet](http://python-future.org/compatible_idioms.html) to scan the script for the tell-tale signs of either (print commands tend to be an easy way of doing this). In this class, we are using Python 3.

There are a number of great Python tutorials available on the web, some can be found here:

+ [Python Docs Tutorials](https://docs.python.org/3/tutorial/)
+ [Python Docs Guide to Tutorials](http://docs.python-guide.org/en/latest/intro/learning/)
+ [Learn Python the Hard Way](https://learncodethehardway.org/python/)
+ [Learn More Python the Hard Way](https://learncodethehardway.org/more-python/)

There are also some excellent Python textbooks and cookbooks. Yes, dear reader, books are still very useful! I recommend the following:

+ Guttag, John. *Introduction to Computation and Programming Using Python*. Cambridge: MIT Press, 2017.
+ McKinney, Wes. 2017. *Python for Data Analysis*. 2nd ed. Boston: O’Reilly Media.

## Python Libraries

Python on its own only provides fairly basic functionality. In order to extend Python, its very large, active, and dedicated user community has contributed an ever-growing list of libraries to make your life easier. A library is a bundle of code that can be easily imported into our current code to add functionality. Libraries define Python objects, functions, and methods that can we can use seamlessly in our own code.

Loading libraries can be computationally expensive (i.e., it consumes resources and slows the execution of any given script); for that reason, Python requires us to explicitly load the libraries that we want to use. For example, say we wanted to load the `math` library and access its `pi` constant:

```python
import math
print(math.pi)
```

Easy peasy! We can also be more specific and import only specific classes, functions, or constants from the library; this will allow you to use simpler syntax. Here, we import only the `math` library's `pi` constant, and print it without having to invoke the library.

```python
from math import pi
print(pi)
```

It is generally considered good practice to keep your imports minimal. In other words, don't load in an entire library if you're only going to use a single class or function.

We can also change the name of the library when it gets imported. This allows you to invoke libraries using shorter names. Libraries often have conventional abbreviations; for example, you'll often see the `pandas` library (which we'll be using a lot in the class!) imported as `pd`.

```python
import pandas as pd
```

If you get an error message stating that "No module named ... ", quit atom. After quitting, install the missing library using pip. For example, in the terminal, to get matplotlib, type 'pip install matplotlib'


### Comments

Comments allow you to include text in you code that is not executed. This makes them exceptionally useful for documenting your code. Documenting your code becomes imperative when you share it. Other coders won't know what was going on in your brain! You probably will have a hard time remembering after a while, too so... do yourself and others a favor. It is always good practice to comment your code with future users (again, including you in two months) in mind. We can have single- or multi-line comments.

Single-line comments start with the hash character, `#` , and extend to the end of the line. A comment may appear at the start of a line or following whitespace or code.

Multiline comments are known as docstrings. They start with “”” and end with “””.

```python
# Firstly, this is a single-line comment.

"""
This is a
multiline
comment
"""

print("Comments worked!")
```

### Variables

Variables allow us to store results, text, functions or data that we can retrieve later by invoking their name. They give our code persistence. Unlike many other programming languages, you don’t have to explicitly define a variable name or its datatype beforehand; you can create variables on the fly! Variables can also be continuously redefined. Python emphasizes legibility. You should as well! Good naming practices clearly refer to the data you are storing.

```python
# We can define variables without having to declare their type. We can name it whatever we want.
x = 4.0
print(x)
print(x * 2)

# A text (or string) variable
text = "This is the text we're storing!"
print(text)

# you can change the value of x as often as you want.
x = 3
print(x)
x = x+2
print(x)

# the following retrieves the value stored in x, adds 2 to it,
# and stores the result in x.
x += 2
print(x)
x -= 10
print(x)

# dividing two integers produces a float
division = 12 / 6
print(division)
print(type(division))
```

## Python Datatypes and Structures

A data structure is a way of organizing data in the computer memory. Data structures can implement one or more particular data types. Some data structures can be built based on a basic type or basic building block. Most languages allow more complicated composite types to be recursively constructed starting from basic types.

### Numeric Types and Their Methods

Python implements four distinct numeric data types: plain integers, long integers, floating point numbers, and complex numbers. In addition, Booleans are a subtype of plain integers.

Variables can be defined based on constructing a numeric data type. Every time we define a variable with a number, we are constructing an instance of the datatype. Different datatypes have different constructors; to construct a numeric data type, you only need to type it! In general, numeric types (and other data types) have associated **methods** and can be manipulated using **operators**.

```python
# Integers (int) are a numerical data-type.
print(1 + 2)
print(type(1 + 2))

# Example of an integer method: .bit_length(), which returns the number of bytes needed to represent the integer in binary
one = 1
one.bit_length()
big = 15000
big.bit_length()

# Floats are another numeric type that allows for fractions.
print(1.0 + .5)
print(3.0 - 2.0)
print(6 * 5.0)
print(7.0 / 2)
print(type(1.0 + 5))

# Example of a float method: .is_integer(), which returns True or False depending on whether the value can be represented as an integer.

flt = 2.5
flt.is_integer()
flt += 0.5
flt.is_integer()
```

Common python operators include: `+`, `-`, `*`, `/`, `//`, `%`, `abs()`, and `int()`. Take a look at the [Python documentation](https://docs.python.org/2/library/stdtypes.html) to see what these do!

### Strings

Strings are sets of characters. We create them by enclosing characters in quotes. Python treats single quotes the same as double quotes, but it's good practice to be consistent with what you use.

Strings can be thought of as lists of characters - we'll get into lists a bit more later. For now, know that we can access substrings by specifying ranges in the list or characters. They also have a number of methods or operations that we can perform with them.

```python
# A string is sequence of characters.
print("Hello World.")

# Let's store a string in a variable called "s".
# Note that using ' and " to define strings are interchangeable.
s = 'This is a string.'
print(s)

# We can access individual characters or substrings. What do you notice about the output from the second print function?
print(s[2])
print(s[2:6])

# You can add strings together (i.e., concatenate them)
string = s + " Another string."
print(string)
string += " A third string."
print(string)

# Examples of string methods: .find(), which returns the index of the first instance of a substring and .count(), which returns the number of occurrences of a particular substring.
string.find("Another")
string.count("i")

```

#### Formatting strings: `f` strings and `str.format()`

Imagine though, that you're interested in including a value stored in a variable in your string. For example, you'd like to print a message to console that includes both the result of an operation and a description of that result. Python now has an simple syntax that accomplishes exactly this, known as the f string. It looks something like this:

```python
result1 = 2.017e-3
print(f"The result of the operation is {result1}!")
result2 = 12.023e-3
print(f"The result of operation one is {result1} and the result of operation two is {result2}!")
```

This simple syntax is a new addition to Python - it only became available in Python 3.6. In prior versions, the same result can be obtained using the `str.format() `method as follows:

```python
finding1 = 17
print("We find that the value is {}!".format(finding1))
finding2 = 13
print("We find that the first value is {} and the second value is {}!".format(finding1, finding2))
```

The `str.format()` method places the variables in curly brackets in the order in which they're passed to the method.


### Booleans
Booleans are binary datatypes that are used to indicate the truth or falsehood of a statement. Epistemologically, computers are incredibly simplistic. They understand two values: `True` and `False` (or 1 and 0). Despite the highly reductive computational treatment of truth they imply, Booleans are exceedingly useful.

```python
# booleans, can hold only two possible values: True or False.
is_true = True
print(is_true)
```

```python
# There are several operators that act on booleans, which can be thought of as constructing Venn diagrams.
# Let x and y be variables storing booleans.
# "Not x" switches the value of x. If x is True, then "not x" is False.
# "x and y" returns True if x and y are True.
# "x or y" returns True if x or y are True.
# Again: Venn diagrams.
x = True
y = False
print(x)
print(not x)
print(x and y)
print(x and not y)
print(x or y)
print(not x or y)
```

```python
# There are functions to make comparisons between values and produce bools.
# '==' tests for equality
print(1 == 2)
print(1 == 1)

# '!=' tests for inequality
print(1 != 2)

# comparison functions also apply to strings
print("abcd" == "abcd")

# Variables and their values can be compared.
x = 1
y = 2

# compare values of variables
print(x == y)

# set x and y to be the same value
x = y
print(x)
print(y)

# check if x and y are THE SAME using the 'is' function.
print(x is y)

x = 1.0
y = 1
print(x == y)
print(x is y)
```

### Lists

Lists are a data structure designed for easy storage and access to data. They are initialized using by using `[ ]` to enclose a comma separated sequence of values. While lists *can* contain a series of values of the same type (integers, floats, etc.), this not required. Lists can comprise a heterogeneous mix of types (e.g., `["whoa, this is", 1, "crazy list", 0.0]`). We can access individual elements of a list, a subset of elements, or the whole list. Lists are mutable: we can modify their elements.

Python deals with multiple data structures in a similar manner. For example lists, dictionaries, files, and and iterators work similarly. It's important to note that Python is 0-indexed. This means that the first element in a list is not accessed with `list[1]`. Rather, it is accessed with `list[0]`. This is the case with most programming languages, with some notable exceptions. `R` for example, is 1-indexed.

```python
l_one = [] # an empty list
x = 5
l_two = [1, 2.0, 'a', "abcd", True, x] # a list containing different values
# lists can be built dynamically (aka on the fly) using the .append() and .extend() methods
l_one.append(1)
l_one.append(2)
print(l_one)
l_three = ['a', 'b', 'c']
l_one.extend(l_three)
l_one.append(l_three)
print(l_one) # Whoa, wait! What's the difference between extend and append?

# Values stored in lists are accessible by their index in the list. Lists maintain their order! We use "[i]" to retrieve the i-th element in a list. Note that the first element in a list in Python has index 0.
alph = ['a', 'b', 'c', 'd', 'e']
print(alph[0])
print(alph[1])

# We can access from the ends of lists as well.
print(alph[-1])
print(alph[-2])

# We can access chunks of a list to produce sub-lists.
print(alph[:2])
print(alph[2:4])

# There is a useful function for producing sequences of numbers.
print(range(10))
print(range(2, 10))
print(range(4, 10, 2))

# The length of a list can be calculated using len()
print(len(range(10)))
```

#### List comprehension

Lists can also be constructed differently using an approach called 'list comprehension'. Basically, what happens here is that a provided operation is applied to each element in a list. This is very, *very* useful in cases where you want to generate a new list that is the result of applying a function or functions to elements of a list - without list comprehension, the syntax would be far more verbose. For example, let's say we want to create a list that is the result of squaring each integer from 0 to 4.

```python
# Verbose syntax without list comprehension
squares = [ ]
for i in range(5):
  squares.append(i * i)
print(squares)

# WITH list comprehension... ahhhhh... it's like taking a warm bath.
squares = [i * i for i in range(5)]
print(squares)
```

If you're familiar with `R`, this is similar to `lapply`.

### Dictionaries

Dictionaries, called "dicts" for short, allow you to store values by providing identifying keys and values. They always have key/value pairs. Dicts are initialized using `{ }`. Placing a comma-separated list of `key:value` pairs within the braces adds initial `key:value` pairs to the dictionary. Dictionaries are indexed by keys instead of numeric indices.

It is best to think of a dictionary as an unordered set of `key:value` pairs, with the requirement that the keys are unique (within one dictionary).

The `keys()` method of a dictionary object returns a list of all the keys used in the dictionary, in an arbitrary order. To check whether a single key is in the dictionary, use the `in` keyword.

```python
d_one = {} # an empty dict
d_two = {'key1':1,'key2':"moose",4:5}
print(d_two)

# Key-value pairs can also be defined like this - note that '6' does NOT refer to an index position like it would with a list. Here, it creates a key (`6`) that is given the value false.
d_two[6] = False
print(d_two)

# values can be retrieved using their keys.
print(d_two['key2'])

# Once again: 6 refers to a KEY, NOT an index position.
print(d_two[6])

# Key-value pairs can be used in conditionals
if not d_two[6]: # evaluates to false
    print("Dicts are fun.")
else:
    print("Dicts are not that fun.")

# The keys and values of dicts can be accessed as lists. Note that, here, they're being converted to strings so that they can be concatenated with the descriptive text.
print("keys: "+str(list(d_two.keys())))
print("values: "+str(list(d_two.values())))

numbers = {'one':1, 'two': 2, 'three': 3}
print(numbers)
print(numbers['one'])
# Hey! This looks familiar... remember list comprehension above? We're using list comprehension to print the dictionary's keys.
print([i for i in numbers])

# We can also use list comprehension to print key:value pairs in a list.
print([(k,v) for k,v in numbers.items()])

list(numbers.values())

# Here, we use the 'values' method to extract dictionary values, which we then convert to a list, which allows us to reference its elements by their index.
playlist = list(numbers.values())
print(playlist[1])
print(list(numbers.keys()))
```

Much like we can create lists using list comprehension, we can construction dictionaries using dictionary comprehension:

```python
mydict = {k:v for (k,v) in zip(range(5), range(5))}
mydict
```

Finally, Python includes a function called `dict` that allows you to use a very intuitive syntax to construct dictionaries.

```python
dict(a = 1, b = 2)
```

## How Python thinks: With objects!

Before we get too much further, it's worth elaborating how Python *thinks*. While this is not a computer science class, I think you'll find that a basic understanding of the stuff under the hood will be helpful. Like most other modern programming languages, Python is *object-oriented*. This means that every variable definition creates an object, or an *instantiation* of an object, to be more precise. These objects can have *methods*, which you'll recognize by their syntax: they look like `.method()`. These will perform some operation on the object on which they're invoked.

### Methods vs. Functions

One common point of confusion for new programmers is the difference between a *method* and a *function*. Both are invoked in code to perform operations. However, they differ in a couple of ways: first of all, a method is bound to a specific type of object. String objects have methods that the programmer can bind to any given instance of the string object. Second of all, a method is automatically passed the object on which it is called. If I have a string variable called `text`, when I use the `.count()` method, `count` is passed the contents of `text`.

A *function*, on the other hand, requires that data be *explicitly passed*. And they are not bound to any particular object, though they may be written to expect certain data types.

Let's consider an example: the difference between the `.sort()` method and the `sorted()` function. Both can be used to sort lists. However, they behave a little bit differently. Consider the following code block:

```python
fun_list = ['are', 'we', 'having', 'fun', 'yet', '?']
fun_list.sort()
print(fun_list)

more_fun = ['i', 'know', 'that', 'i', 'am', '!']
more_fun_sort = sorted(more_fun)
print(more_fun_sort)
```

Both the list object's `.sort()` method and the `sorted()` function sort the elements of a list. One modifies the list in place and the other returns a new sorted list. This isn't really what we're interested in here, though. Take a look at the invocation of `fun_list.sort()`: `fun_list` is automatically implicitly passed to the `.sort()` method. `sorted()` on the other hand requires that we be explicit and pass the `more_fun` variable.

This will make more sense as you work with functions and methods; keep it in mind, though, as we begin to explore Python's capabilities in earnest.

## Flow Control

Okay, we've started getting the hang of Python data structures and how they can be manipulated. But a program that flows linearly through a long list of variable definitions and commands is pretty limited; say we want our program to make decisions based on values of a variable! Say we want our program to perform a task over and over again until it reaches a given state! Say we find ourselves writing the same basic commands over and over again and want a more efficient way of invoking those commands! We can do all of this and more with what we call 'control flow'. In Python there are three main categories of program control flow:

+ Branches
+ Loops
+ Function calls

### Branches

You can think of branches as decisions based on criteria you provide. If-elif-else statements execute a block of code if a given condition is true, and a different block of code if a given condition is false. Take note of the syntax in the below example: `if [statement]:` is followed by a line break, then a tab. If you do not follow this syntax, your code will not work correctly! Python is somewhat distinctive in that it reads meaning into levels of indentation; it *interprets* some types of *whitespace*. The code that is indented one level (one tab) below an if-elif-else statement will be executed when that statement's condition is true. The same holds true for loops and function calls, as we'll see below.

```python
flag = True
if flag:
    x = 1
    print("Flag is True.")
else:
    x = 2
    print("Flag is False.")
print(x)

# We can check for other cases as well. The == operator checks for equivalence,
# so it will be true when x is equal to a given value
if x == 0:
    print("A")
elif x == 1:
    print('B')
else:
    print("C")
```

### Loops

Loops allow us to automate repetitive tasks (hooray!). Repeatedly executing a set of statements is called *iteration*. There are a number of way to iterate in Python. We can use `for` loops or `while` loops. The syntax is like the syntax of if-statements---notice the indentations! The `for` loop loops over each of the elements of a list or iterator, assigning the current element to the variable name given. A `while` loop repeats a sequence of statements until some condition becomes false.


```python
x = range(10)
print(x)

for i in x:
    print(i)

for i in x:
    # doubles the list element
    print(i*2)
```

We can control the execution of a loop through branches. Python includes statements to exit a loop prematurely. To exit a loop, use the `break` statement.


```python
for i in range(10):
    if (i > 5):
        break # breaks out of the loop when it gets a number higher than five
    print(i) # How would the output of this code change if this statement was before the if-statement?
```

You can iterate through lists using a uniquely simple syntax. This, incidentally, is one of the strengths of Python---it can loop through lists very, very intuitively.

```python
myList = ["This", "is", "Python"]
for i in myList:
    print(i) # print the value
    print(myList.index(i)) # print the position of the value (index)
```

Build a list that contains all the courses that you are taking this semester. Then, construct a for loop that prints them. Every time you print a course number add the phrase `In Spring 2018, I am taking:`. Remember that you can use the `f` string syntax we discussed above!

```python
# Your code here

```

### Functions
Functions allow a programmer to write reusable code that performs an action predictably wherever it is invoked. Functions make your code modular, and permit you to efficiently reuse chunks of code. Once a function is defined, it can be called by typing the name of the function and passing the arguments you've defined. For example, Python gives you many built-in functions like `print()`. Functions can just perform an operation, or they can return values.

Functions are defined using the key word `def`. As with the other flow control types we've seen, we use indentation to indicate the portion of our code that's part of the function definition.

```python
# Consider this example!
# First choose an initial value for x.
x = 0
for i in range(100):
    x += i
print(x)

# What if we want to do this for a new initial value for x? What if we use a different number instead of 100? We don't want to rewrite this for loop every time, so let's define a function!
def for_sum(x, y):
    for i in range(y):
        x += i
    # "return" indicates what values to output
    return x

# Same calculation from above
print(for_sum(0,1 00))
print(for_sum(10, 50)) # Now with new numbers

# Interestingly, variables can store functions. This means that functions
# can be inputs to other functions.
f = for_sum
print(f(0, 100))

def execute(funct, x):
    return funct(x, 100)

print(execute(f, 10))

# Now, just for fun:
print(f(f(f(10, 100), 50), 1000))
```

```python
def print_words(x = "This", y = "Not Eric"):
    print(x)
    print(y)

print_words()

x = "Eric"
y = "Something else"

print_words(x, y)
```

Now, wrap the code you created for the previous section in a function called `course_printer`.

```python
# Your code here:

```

### `numpy` Arrays and Vectorization

`numpy` arrays are a bit different from regular Python lists. It's important to note this up front because these are the bread and butter of data science in Python. `pandas` series are built atop them.

To speak technically, operations on `numpy` arrays, and by extension, `pandas` series, are **vectorized**. You can add two numpy lists by just using `+`. You have seen this in idea in spreadsheets, at least if you've ever added an entire column to another one. This would not work with a standard Python list! To add regular Python lists elementwise (i.e., element by element), you would need to use a rather cumbersome loop:

```python
# import the numpy package
import numpy as np

# without vectorized numpy arrays
a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]
c = []
for i, j in zip(a, b):
  c.append(i + j)
print(c)

# with vectorized numpy arrays
a = np.array([1, 2, 3, 4, 5])
b = np.array([6, 7, 8, 9, 10])
c = a + b
print(c)
```
**Vectorization** is a powerful idiom, and we will use it a lot in this class. For almost all data intensive computing, we will use `numpy` arrays rather than Python lists.

## Fin.

Okay, so that was a lot. Obviously, you should not expect all of this to stick immediately. Hopefully, though, the waters will begin to clear as you tackle the problem set for this week.
