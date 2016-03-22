# Simple program to calculate the spam score from given text file that contains all headers.
# Use the file name testinput.txt as the file name.
# Sample file:
# asdf
# whatever
# X-DSPAM-Confidence:    0.8475
# asdfa
# X-DSPAM-Confidence:    0.9999
# sd
# X-DSPAM-Confidence:    0.231
# a
# X-DSPAM-Confidence:    1.1

fname = input("Enter file name (testinput.txt): ")
fh = open(fname)
total = 0.0
counter = 0
str2 = "X-DSPAM-Confidence:"
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue

    startIndex = len(str2)
    endIndex = len(line)

    strNumber = line[startIndex:endIndex].rstrip()
    myFloat = float(strNumber)
    total = total + myFloat
    counter = counter + 1

average = total / counter
print ("Average spam confidence: " + str(average))
