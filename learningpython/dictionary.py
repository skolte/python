__author__ = 'sandeep'
#9.4 Write a program to read through the mbox-short.txt and figure out who has the sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
dictionary = dict()

for line in handle:
    if(line.startswith('From ')):
        words = line.split() # split on spaces
        dictionary[words[1]] = dictionary.get(words[1], 0) + 1

maxKey = None
maxValue = None
for myKey, myValue in dictionary.items():
	if maxValue == None or myValue > maxValue:
		maxValue = int(myValue)
        	maxKey = myKey
        #print myKey + ' ' + str(myValue)
        #print maxKey + ' ' + str(maxValue)

print (maxKey + ' ' + str(maxValue))

#desired output cwen@iupui.edu 5