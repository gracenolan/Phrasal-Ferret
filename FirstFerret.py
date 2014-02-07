#! /usr/bin/python3

import codecs
from lxml import etree  # Lets use this as the xml parser, it has some more features :D
import sys
import fnmatch

# This is Phrasal Ferret's collection of phrases 
# dictionary of phrases with a count of how often they appear 
phrases = {}

# Phrasal Ferret wants some new phrases! Will he find anything?
# He looks through the leaves (elements) to see what he can find
def print_all():
  root = tree.getroot()
  allChars = root.findall(".//*[@font]")
  for char in allChars:
    print(char.text)

# globals to hold continuity of phrases
font = ""
bold_phrase = ""
# Phrasal Ferret thinks bold phrases are damn tasty
# this function finds all of the bold phrases
def find_bold(textline):
  global bold_phrase
  global font

  for text in textline:
    if not text.tag == "text":
      continue

    # Is this char part of the current phrase?
    if text.get("font"):
      if font == text.get("font"):
        bold_phrase += text.text 

      # is this the start of a a new phrase?
      elif "Bold" in text.get("font"):
        # save the last phrase before starting a new one
        if len(bold_phrase) > 2: 
          if not bold_phrase in phrases:
            phrases[bold_phrase] = 1
          else:
            phrases[bold_phrase] += 1

       # clear old phrase and save the new one
        bold_phrase = text.text
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

          find_bold(textline)

# Read in the file name
if len(sys.argv) != 2:
  print("Usage: FirstFerret.py <xml file> \nPhrasel Ferret likes to climb xml trees. They have the softest leaves and pleasant smelling flowers. Please try again with an xml file >^_^<")
  raise SystemExit
elif fnmatch.fnmatch(sys.argv[1], "*.xml"): 
  filename = sys.argv[1]
  try:
    parser = etree.XMLParser(recover=True)
    tree = etree.parse(codecs.open(filename, encoding = "UTF-8", errors='replace'), parser=parser) # build tree. This is where the error is occuring!
  except:
    print("OH NO. Phrasal Ferret fell from the branch. (Looks like something went wrong)") 
  find_text()
else:
  print("Phrasel Ferret farts in your general direction.")

print(str(len(phrases)) +  " bold phrases found")
key = max(phrases, key=phrases.get)
print("The most common Bold phrase is:")
print(key, phrases[key])
print("done")
raise SystemExit

