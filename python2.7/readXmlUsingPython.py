# Read xml document using python.
import urllib
import xml.etree.ElementTree as ET

serviceurl = 'http://python-data.dr-chuck.net/comments_244391.xml'

uh = urllib.urlopen(serviceurl)
data = uh.read()
tree = ET.fromstring(data)

counts = tree.findall('.//count')
mysum = 0
for count in counts:
    mysum = mysum + int(count.text)
print mysum
