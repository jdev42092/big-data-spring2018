###################################################
## PS1- Intro to Python                          ##
## 11.S947: Big Data, Visualization and Society  ##
## By Jay Dev                                    ##
###################################################

# Import packages
import math
from random import randint

# A. LISTS
## A.1 Create a list containing 4 strings

anyfourstrs = ['juggling', 'sous viding', 'boxing', 'needlepointing']

## A.2 Print the 3rd item in the list
print(anyfourstrs[2])

## A.3 Print the 1st and 2nd item
print(anyfourstrs[0:2])

## A.4 Add a new string to the end of the list
anyfourstrs.append('last')
print(anyfourstrs)

## A.5 Get the list length
print(len(anyfourstrs))

## A.6 Replace the last item in the list
anyfourstrs[4] = 'new'
print(anyfourstrs)

#----------------------------------------------------#

# B. STRINGS

sentence_words = ['I', 'am', 'learning', 'Python', 'to', 'munge', 'large', 'datasets', 'and', 'visualize', 'them']

## B.1 Convert the list into a normal sentence
norm_sentence = " "
norm_sentence = norm_sentence.join(sentence_words)
print(norm_sentence)

## B.2 Reverse the order of this list
sentence_words.reverse()
print(sentence_words)

## B.3 Sort the list using the default sort order
sentence_words = ['I', 'am', 'learning', 'Python', 'to', 'munge', 'large', 'datasets', 'and', 'visualize', 'them']
sentence_words.sort()
print(sentence_words)

## B.4 Perform the same operation using the sorted() field
sentence_words = ['I', 'am', 'learning', 'Python', 'to', 'munge', 'large', 'datasets', 'and', 'visualize', 'them']
secondsort = sorted(sentence_words)
print(secondsort)

## Describe how sort() and sorted() differ
"""
The METHOD .sort() and the FUNCTION sorted() differ in a couple ways (from the Python 3.3.7 Documentation):
  1. sorted() takes any iterable (e.g., a list, string, or tuple) as an input, whereas .sort() can only be used on lists
  2. .sort() modifies a list in-place (that is, it returns none and modifies the original object), whereas sorted() returns a new sorted list
"""

## B.5 (EXTRA CREDIT) Modify the sort to do a case case-insensitive alphabetical sort
case_insensitive = sorted(sentence_words, key=str.lower)
print(case_insensitive)

#----------------------------------------------------#

# C. RANDOM FUNCTION
# INPUT: Two integers that will be used as lower and upper bounds of the function. If the user does not pass a lower bound, the default value should be zero.
# OUTPUT: Print a random number within the established bounds

def rand_optional(high, low=0):
    return(randint(low,high))

print(rand_optional(100))
print(rand_optional(100, low=50))

assert(0 <= rand_optional(100) <= 100)
assert(50 <= rand_optional(100, low = 50) <= 100)
#----------------------------------------------------#

# D. STRING FORMATTING FUNCTION
# INPUT: An integer representing the position on the bestseller list and a string representing the a title. If not already titlecased, the function should titlecase the string.
# OUTPUT: Print a string of the format: The number n bestseller today is: title. You should use an f string or the .format() method to format the printed string.

def bookrank(title, rank):
    print(f"The number {rank} bestseller today is: {title.title()}")

bookrank("theft by finding: diaries (1977-2002)",117)

#----------------------------------------------------#

# E. PASSWORD VALIDATION FUNCTION
# INPUT: A string that will be tested for the password requirements. The string can be passed as an argument to the function, or as an input through the input function.
# OUTPUT: A success message if the password works, an error message if it fails.
# Password Requirements:
    # is 8-14 characters long
    # includes at least 2 digits (i.e., numbers)
    # includes at least 1 uppercase letter
    # includes at least 1 special character from this set: ['!', '?', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=']


def pwdvalid(pwd):
    if (8 <= len(pwd) <= 14) and (sum([d.isdigit() for d in pwd]) >= 2) and (sum([u.isupper() for u in pwd]) >= 1) and (sum([c in ['!', '?', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '='] for c in pwd]) >=1):
        print("Huzzah! This is a strong password!")
    else:
        print("ERROR: YOUR PASSWORD DOESN'T FIT THE CRITERIA.")
# Testing criteria
## Too short
pwdvalid("Iiii11!")
## Too long
pwdvalid("Iii111!!Iii111!!")
## No Uppercase
pwdvalid("iii111!!")
## Not enough digits
pwdvalid("Iiiii1!!")
## No special characters
pwdvalid("Iii11111")
## This one works
pwdvalid("Iii111!!")
#----------------------------------------------------#

# F. EXPONENTIATION FUNCTION
# INPUT: i) An integer that will be recursively multiplied, and ii) An integer that will define the number of times to multiply the number to get the exponentiation.
## May assume inputs are positive integers
# OUTPUT: An integer that is the result of the exponentiation.
def exp(base,exponent):
    i = 0
    result = 1
    while i < exponent:
        result = result * base
        i = i + 1
    return(result)
exp(2, 3)
exp(5, 4)
exp(5,0)
#----------------------------------------------------#

# G. (EXTRA CREDIT) MIN AND MAX FUNCTIONS
# INPUT: A list of numbers to be tested.
# OUTPUT: A number of the list that is the maximum or minimum.

def user_max(values):
    max = values[0]
    for v in values:
        if v > max:
            max = v
    return(max)

user_max([1, 3, 4, 5, 5, 7])
user_max([9, 9, 9, 9, 9, 9])

def user_min(values):
    min = values[0]
    for v in values:
        if v < min:
            min = v
    return(min)

user_min([1, 3, 4, 5, 5, 7])
user_min([9, 9, 9, 9, 9, 9])
