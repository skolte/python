# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
total = 0.0
counter = 0
str2 = "X-DSPAM-Confidence:"
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue

    startIndex = len(str2)
    endIndex = len(line)
    #print('Start:'+str(startIndex) + ' end: ' + str(endIndex))
    strNumber = line[startIndex:endIndex].rstrip()
    #print("str:" + strNumber)
    #abc = input("whatever:")
    myFloat = float(strNumber)
    #print(str(myFloat))
    total = total + myFloat
    counter = counter + 1
    #print(str(total))
    #print(str(counter))
average = total / counter
print ("Average spam confidence: " + str(average))
