# Read json document and calculate the sum of all counts.
# This code uses Python 2.7.

import json
from urllib.request import urlopen

while True:
    address = raw_input('Enter location: ')
    url = raw_input('Enter location:')
    print 'Retrieving ' + url
    with urllib.request.urlopen(url) as url:
        response = url.read()
        comments = json.loads(response)
        print ('User count:', len(comments))

    totalCount = 0
    commentsCollection = comments["comments"]
    for comment in commentsCollection:
            totalCount += int(comment["count"])

    print(totalCount)

