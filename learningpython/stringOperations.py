# Some simple string manipulations.
__author__ = 'sandeep'
text = "X-DSPAM-Confidence:    0.8475";
numPosition = text.find("0.8475");
print (numPosition)
if numPosition != -1:
    length = len(text)
    print (float(text[numPosition:len(text)]))