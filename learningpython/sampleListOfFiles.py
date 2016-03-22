# A simple program to read a given file and count number of lines that start with 'From '.
# This one doesn't use a regex.
__author__ = 'sandeep'

fname = input("Enter file name (mbox-short.txt): ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0

lst = list()
for line in fh:
    if line.startswith('From '):
        words = line.split()
        if len(words) > 1:
            address = words[1]
            print(address)
            lst.append(address)
            count = count + 1

print ("There were", count, "lines in the file with From as the first word")
