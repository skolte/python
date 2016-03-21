__author__ = 'sandeep'

x = (5, 1, 3)
if (4,100,200) > x :
    print ('yes1')
if (0,1000,2000) > x :
    print ('yes2')
if (6, 0, 0) > x :
    print ('yes3')
if (5, 0, 300) > x :
    print ('yes4')

name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

dictionary = dict()
for line in handle:
    if(line.startswith('From ')):
        words = line.split() # split on spaces
        hourWord = words[5]
        hour = hourWord[0: 2]
        dictionary[hour] = dictionary.get(hour, 0) + 1

myList = list()
for key, val in dictionary.items():
	myList.append((key, val))

myList.sort()

for key, val in myList:
    print (key, val)