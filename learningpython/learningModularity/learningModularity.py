# Learning how to restructure your python code to create modules, functions from a simple routine.
# this introduces a function so that module can be imported and then the function can be executed on demand.
# you can't still run the module from command line.
# Add __name__ at the very end.
# Sandeeps-MacBook-Pro:learningModularity sandeep$ python3 learningModularity.py
# __main__
# then wrap it in a 'if' statement.
# Sandeeps-MacBook-Pro:learningModularity sandeep$ python3 learningModularity.py
# and it prints the whole list.

from urllib.request import urlopen

def fetch_words():
	with urlopen('http://sixty-north.com/c/t.txt') as story:
		story_words = []
		for line in story:
			line_words = line.decode('utf-8').split()
			for word in line_words:
				story_words.append(word)

	for word in story_words:
		print (word)

#print (__name__)
if __name__ == '__main__':
	fetch_words()