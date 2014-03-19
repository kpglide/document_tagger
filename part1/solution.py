import re
import sys
from pg_sample_texts import DIV_COMM, MAG_CART
documents = [DIV_COMM, MAG_CART]

# Create regular expressions to search for the
# title, author, translator and illustrator of a
# Project Gutenberg text.

title_search = re.compile(r'(title:\s*)(?P<title>(.+\n)*)', re.IGNORECASE)
author_search = re.compile(r'(author:)(?P<author>.*)', re.IGNORECASE)
translator_search = re.compile(r'(translator:)(?P<translator>.*)', re.IGNORECASE)
illustrator_search = re.compile(r'(illustrator:)(?P<illustrator>.*)', re.IGNORECASE)

# Iterate over each text and extract and print the title,
# author, translator and illustrator metadata
# for each one. 

for i, doc in enumerate(documents):
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
  print "***" * 25
  print "Here's the Title, Author, Translator and Illustrator " \
        "info for doc {}:".format(i)
  print "\n"
  print "Title:  {}".format(title)
  print "Author(s): {}".format(author)
  print "Translator(s): {}".format(translator)
  print "Illustrator(s): {}".format(illustrator), "\n"

# Accept user-supplied keywords from the command line, and
# create regular expressions to search for the keywords.

  searches = {}
  for kw in sys.argv[1:]:
    searches[kw] = re.compile(r'\b' + kw + r'\b', re.IGNORECASE)

# Iterate over each text and use the regular
# expressions to search for the keywords.
# Print the keywords and number of times
# they appear in the text.

  print "Here's the keyword info for doc {}:".format(i)
  for search in searches:
    print "\"{0}\": {1}".format(search, len(re.findall(searches[search], doc)))