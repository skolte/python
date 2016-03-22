# Learning how to restructure your python code to create modules, functions from a simple routine.
# this introduces a function so that module can be imported and then the function can be executed on demand.
# you can't still run the module from command line.

# added further refactoring so that printing method is separate now.
# Also, we now add main() function so that we can test it from the REPL.

# Running from REPL:
# python3
# >>> from learningModularity import (fetch_words, print_words)
# >>> print_words(fetch_words())

from urllib.request import urlopen

def fetch_words():
	with urlopen('http://sixty-north.com/c/t.txt') as story:
		story_words = []
		for line in story:
			line_words = line.decode('utf-8').split()
			for word in line_words:
				story_words.append(word)
		return story_words

def print_words(story_words):
	for word in story_words:
		print (word)

def main():
	words = fetch_words()
	print_words(words)

if __name__ == '__main__':
	main()