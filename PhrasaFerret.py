#! /usr/bin/python3

import codecs
from lxml import etree  # Lets use this as the xml parser, it has some more features :D
import sys
import fnmatch
import ScholarScrape

# This is Phrasal Ferret's collection of global variables
phrases = {}          # Dictionary of phrases and frequencies 
filename = ""
doc = ""              # Holds the plain text vers of the doc
font = ""             # keep track of fonts used (for finding italics)
italic_phrase = ""    # temp phrase value 
last_text_size = 0    # value to track varing font sizes (for finding title)
title = ""
temp = ""             # holds the temporary title 
size = 0
page = 0

# Phrasal Ferret wants some new phrases! But first it needs plain text, not xml
# It strips the branches of all the useful leaves to get plain text
def extract_xml():
  global doc
  root = tree.getroot()
  allChars = root.findall(".//text")
  for char in allChars:
    try:
      doc += char.text
    except:
      continue
  find_repeats() # this calls the function that raises the error

# Phrasal Ferret liked those italic phrases so much
# Now it wants to find those phrases again!
# This looks for repeats of phrases in the document. 
# Note: only accepts plain text, not xml.
def find_repeats():
  global doc
  global phrases
  for key, value in phrases.items():
    appearances = doc.count(key) # this is the broken line of code
    #if phrase in doc:
    phrases[key] += appearances

def get_title(text):
  global title
  global size
  global last_text_size # is -1 if title ended
  global temp

  # is this a text element with a size?
  if text.get("size"):
    size = float(text.get("size"))

  if size > last_text_size:
    last_text_size = size
    temp = text.text

  elif size == last_text_size:
    temp += text.text 

  elif size < last_text_size:
    temp = temp.strip()
    if len(temp) > len(title): # assuming titles will be the biggest and longest
       title = temp

  else: # if there is no char in this element, add a space
    temp += " "


# Phrasal Ferret thinks italic phrases are damn tasty
# this function finds all of the italic phrases
def find_italic(textline):
  global italic_phrase
  global font
  global size
  global last_text_size
  global page

  for text in textline:
    if not text.tag == "text":
      continue

    # Grab the title from the first page
    if page == '1':
      get_title(text)

    # Is this char part of the current phrase?
    if text.get("font"):
      if font == text.get("font"):
        italic_phrase += text.text 

      # is this the start of a a new phrase?
      elif "Italic" in text.get("font"):
        # save the last phrase before starting a new one
        if len(italic_phrase) > 2:
          italic_phrase = italic_phrase.strip()
          if not italic_phrase in phrases:
            phrases[italic_phrase] = 1
          else:
            phrases[italic_phrase] += 1

        # clear old phrase and save the new one
        italic_phrase = text.text
        font = text.get("font")

      else:
        continue
    elif len(italic_phrase) > 0: # if there is no font, add a space
      italic_phrase += " "

# Phrasal Ferret excitedly wiggles it's nose! 
# It scuttles along the branches in search for tasty text he can analyse. 
def find_text():
  global page

  root = tree.getroot()

  # are there leaves on this tree?
  if len(root):
    print("lets climb some branches!")

    # climb through the first branches
    for child in root:

      # Grab the page number
      if child.tag == "page":
        page = child.get("id")

      # Get the textbox
      for textbox in child:
        if not textbox.tag == "textbox":
          continue

        # Get the textline
        for textline in textbox:
          if not textline.tag == "textline":
            continue

          find_italic(textline)

def search_google():
  query = raw_input("Would you like to search Google Scholar for this paper and its most common phrase? yes/no\n")
  if query == "yes":
    print("Searching...")
    ScholarScrape.search(title + key)
  elif query == "no":
    print("done")
    raise SystemExit
  else:
    print("**Please choose 'yes' or 'no'**")
    search_google()


# ---- This is Phrasal Ferret's starting point, the first block of the program  ---- #

if len(sys.argv) != 2:
  print("Usage: FirstFerret.py <xml file> \nPhrasel Ferret likes to climb xml trees. They have the softest leaves and pleasant smelling flowers. Please try again with an xml file >^_^<")
  raise SystemExit

elif fnmatch.fnmatch(sys.argv[1], "*.xml"): 
  filename = sys.argv[1]
  try:
    parser = etree.XMLParser(recover=True)
    tree = etree.parse(codecs.open(filename, encoding = "UTF-8", errors='replace'), parser=parser)
  except:
    print("OH NO. Phrasal Ferret fell from the branch. (Looks like something went wrong)")
    raise SystemExit

  find_text()
else:
  print("Phrasel Ferret farts in your general direction.")

# convert to plain text and find recurrances 
extract_xml()

# What did Phrasal Ferret find? Here are the results 
print(str(len(phrases)) +  " italic phrases found")
key = max(phrases, key=phrases.get)
print("The most common italic phrase is:")
print(key, phrases[key])
print("title: " + title)

search_google()
