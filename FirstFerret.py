#! /usr/bin/python3

import codecs
from lxml import etree  # Lets use this as the xml parser, it has some more features :D
import sys
import fnmatch

# This is Phrasal Ferret's collection of phrases 
# dictionary of phrases with a count of how often they appear 
phrases = {}
filename = ""
doc = "" 
# Phrasal Ferret wants some new phrases! Will he find anything?
# He looks through the leaves (elements) to see what he can find
def extract_xml():
  global doc
  root = tree.getroot()
  allChars = root.findall(".//*[@font]")
  for char in allChars:
    try:
      doc += char.text
    except:
      continue
    #print(doc)
  find_repeats() # this calls the function that raises the error

# find repeats of phrases in the document. 
# Note: only accepts plain text, not xml
def find_repeats():
  global doc
  global phrases
  for key, value in phrases.items():
    appearances = doc.count(key) # this is the broken line of code
    #if phrase in doc:
    phrases[key] += appearances


# globals to hold continuity of phrases
font = ""
italic_phrase = ""
# Phrasal Ferret thinks italic phrases are damn tasty
# this function finds all of the italic phrases
def find_italic(textline):
  global italic_phrase
  global font

  for text in textline:
    if not text.tag == "text":
      continue

    # Is this char part of the current phrase?
    if text.get("font"):
      if font == text.get("font"):
        italic_phrase += text.text 

      # is this the start of a a new phrase?
      elif "Italic" in text.get("font"):
        # save the last phrase before starting a new one
        if len(italic_phrase) > 2: 
          if not italic_phrase in phrases:
            phrases[italic_phrase] = 1
          else:
            phrases[italic_phrase] += 1

       # clear old phrase and save the new one
        italic_phrase = text.text
        font = text.get("font")

      else:
        continue

# Phrasal Ferret excitedly wiggles it's nose! 
# It scuttles along the branches in search for tasty text he can analyse. 
def find_text():
  root = tree.getroot()

  # are there leaves on this tree?
  if len(root):
    print("lets climb some branches!")

    # climb through the first branches
    for child in root:

      # Get the textbox
      for textbox in child:
        if not textbox.tag == "textbox":
          continue

        # Get the textline
        for textline in textbox:
          if not textline.tag == "textline":
            continue

          find_italic(textline)


# ---- This is where the first block of the program where the file is read ---- #

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

# grab the plain txt version of the file for easier reinforcement scanning
filename.replace(".xml", ".txt")
try:
  doc = open(filename, encoding= "UTF-8")
except:
  print("it would have been nice if you extracted that doc as a .txt file too. Makes it easier for scanning ^_^")
  extract_xml()

# What did Phrasal Ferret find? Here are the results 
print(str(len(phrases)) +  " italic phrases found")
key = max(phrases, key=phrases.get)
print("The most common italic phrase is:")
print(key, phrases[key])



print("done")
raise SystemExit

