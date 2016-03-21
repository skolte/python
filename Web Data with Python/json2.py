# This code uses Python 3.4.2
import json
from urllib.request import urlopen

while True:
    url = input('Enter location: ')
    if len(url) < 1 : break

    print ('Retrieving :', url)
    response = urlopen(url).read().decode('utf8')
    print ('Retrieved',len(response),'characters')

    comments = json.loads(response)
    totalCount = 0
    commentsCollection = comments["comments"]

    print ('Count:', len(commentsCollection))
    for comment in commentsCollection:
            totalCount += int(comment["count"])

    print('Sum:', totalCount)
