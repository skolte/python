# Learning how to restructure your python code to create modules, functions from a simple routine.
# this introduces a function so that module can be imported and then the function can be executed on demand.
# To run on REPL:
# python3
# >>> import learningModularity
# >>> learningModularity.fetch_words()
# At this point, it should print a list of words obtained from 'http://sixty-north.com/c/t.txt'.
# However you can't still run the module from command line.

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
