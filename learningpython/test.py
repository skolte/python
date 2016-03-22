# Playing with conversion to int.

#astr = 'Hello Bob'
#istr = int(astr)
#print 'First', istr
#astr = '123'
#istr = int(astr)
#print 'Second', istr

astr = 'Hello Bob'
istr = 0
try:
    istr = int(astr)
except:
    istr = -1
print istr