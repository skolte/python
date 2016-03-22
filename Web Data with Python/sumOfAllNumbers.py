# Read a text file, use regular expression to get sum of all numbers in the file.
__author__ = 'sandeep'
import re
with open('regex_sum_244389.txt', 'r') as f:                        # Open and read the file.
    print (sum([int(s) for s in re.findall("[0-9]+",f.read())]))    # Find all numbers using regular expression and findall(). Sum them. Print the sum.
f.closed                                                            # Close the file.