# Simple program that shows how to use a regular expression to find a sub-string in a string.
# Input :  'From: Using the : character'
# Search occurrences of 'From:'
import re
x = 'From: Using the : character'
y = re.findall('^F.+:', x)
print (y)