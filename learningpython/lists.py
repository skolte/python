# Accept a filename for a file that has list of words, print the list.
__author__ = 'sandeep'
fname = raw_input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    words = line.split()
    for word in words:
        if word not in lst:
    		lst.append(word)

lst.sort()
print (lst)