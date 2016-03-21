# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program
# Following Links in Python

# In this assignment you will write a Python program that expands on http://www.pythonlearn.com/code/urllinks.py. The program will use urllib to read the HTML from the data files below, extract the href= vaues from the anchor tags, scan for a tag that is in a particular position relative to the first name in the list, follow that link and repeat the process a number of times and report the last name you find.
#
# We provide two files for this assignment. One is a sample file where we give you the name for your testing and the other is the actual data you need to process for the assignment
#
# Sample problem: Start at http://python-data.dr-chuck.net/known_by_Fikret.html
# Find the link at position 3 (the first name is 1). Follow that link. Repeat this process 4 times. The answer is the last name that you retrieve.
# Sequence of names: Fikret Montgomery Mhairade Butchi Anayah
# Last name in sequence: Anayah
# Actual problem: Start at: http://python-data.dr-chuck.net/known_by_Dilraj.html
# Find the link at position 18 (the first name is 1). Follow that link. Repeat this process 7 times. The answer is the last name that you retrieve.
# Hint: The first character of the name of the last page that you will load is: K
__author__ = 'sandeep'

import urllib
import re
from BeautifulSoup import *
url = raw_input('Enter URL:')
count = int(raw_input("Enter count:"))
position = int(raw_input("Enter position:"))
position = position - 1 # zero based
myposition = 0
prefix = re.search('known_by_', url)
suffix = re.search('\.html', url)
name = url[prefix.end():suffix.start()]
for x in range(count):
    print ('Retrieving: '+url)
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    for link in soup.findAll('a', href=True):
        if myposition == position:
            name = str(link.text)
            url = str(link.get('href'))
            myposition = 0
            break
        else:
            myposition += 1

print ('Retrieving: '+url)
