import re
import sys
import os

def file_opener(directory):
	
	# Find all text files in a directory, open
	# them and add their contents to a list.

	documents = []
	for fl in (os.listdir(directory)):  
		if fl.endswith('.txt'):       
			fl_path = os.path.join(directory, fl) 
			with open(fl_path, 'r') as f:         
				documents.append(f.read())        
   	return documents

def get_gutenberg_header(doc):

	# Iterate over each text, and extract and print the title,
	# author, translator and illustrator metadata
	# for each one. 

	title_search = re.compile(r"(title:\s*)(?P<title>.+\n(  +.+)*)", re.IGNORECASE)
	author_search = re.compile(r'(author:)(?P<author>.*)', re.IGNORECASE)
	translator_search = re.compile(r'(translator:)(?P<translator>.*)', re.IGNORECASE)
	illustrator_search = re.compile(r'(illustrator:)(?P<illustrator>.*)', re.IGNORECASE)
	title = re.search(title_search, doc).group('title')
	author = re.search(author_search, doc)
	translator = re.search(translator_search, doc)
	illustrator = re.search(illustrator_search, doc)
  	
  	if author: 
  		author = author.group('author')
  	if translator:
  		translator = translator.group('translator')
  	if illustrator:
  		illustrator = illustrator.group('illustrator')
  	print "Here's the Title, Author, Translator and Illustrator " \
        "info:", "\n"
	print "Title:  {}".format(title)
	print "Author(s): {}".format(author)
	print "Translator(s): {}".format(translator)
	print "Illustrator(s): {}".format(illustrator), "\n"

def  key_word_regexes(keywords):

	# Create a regular expression for each keyword
	# in the keywords list and returns a 
	# dictionary of the keywords and their regular expressions

	searches = {}
	for kw in keywords:
		searches[kw] = re.compile(r'\b' + kw + r'\b', re.IGNORECASE)
	return searches

def find_keywords(searches, doc):
	
	# Accepts a dictionary of keywords and corresponding
	# regular expressions, aka searches, as 
	# a param and finds them in the doc

	print "Here's the keyword info:", "\n"
	for search in searches:
		print "\"{0}\": {1}".format(search, len(re.findall(searches[search], doc)))
	print "\n"

def main(argv=sys.argv):
	documents = file_opener(sys.argv[1])
	searches = key_word_regexes(sys.argv[2:])
	for i, doc in enumerate(documents):
		print "***" * 10
		print "For document {}:".format(i), "\n"
		get_gutenberg_header(doc)
		find_keywords(searches, doc)

if __name__ == '__main__':
	main()