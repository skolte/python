# Using a regular expression
import re
mystr = '<p>Please click <a href="http://www.dr-chuck.com">here</a></p>'

a = re.findall('href=\"(.+)\"', mystr)
print (a)