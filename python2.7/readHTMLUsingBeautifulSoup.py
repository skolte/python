# This is a simple python program to read HTML page, use BeautifulSoup, and count the number of 'span' elements.
# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# into the same folder as this program

import urllib
from BeautifulSoup import *

url = 'http://python-data.dr-chuck.net/comments_244394.html'
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)

# Retrieve all of the anchor tags
spans = soup('span')
mysum = 0
for span in spans:
    # Look at the parts of a tag
    mysum = mysum + int(span.text)
print 'sum:',mysum