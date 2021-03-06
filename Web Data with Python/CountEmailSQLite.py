import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('''
DROP TABLE IF EXISTS Counts''')

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

fname = 'mbox.txt' #input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox-short.txt'
fh = open(fname)
for line in fh:
	if not line.startswith('From: ') : continue
	organizationIndex = line.find('@', 0, len(line))
	#spaceIndex = line.find(' ', organizationIndex, len(line))
	if organizationIndex > -1:
		organization = line[organizationIndex + 1:len(line)]
		organization = organization.rstrip()
		#print(organization)
		cur.execute('SELECT count FROM Counts WHERE org = ? ', (organization,))
		row = cur.fetchone()
	if row is None:
		cur.execute('''INSERT INTO Counts (org, count)
                    VALUES ( ?, 1 )''', (organization,))
	else:
		cur.execute('UPDATE Counts SET count=count+1 WHERE org = ?',
		            (organization,))
	# This statement commits outstanding changes to disk each
	# time through the loop - the program can be made faster
	# by moving the commit so it runs only after the loop completes
	conn.commit()

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

print
print("Counts:")
for row in cur.execute(sqlstr):
	print(str(row[0]), row[1])

cur.close()
