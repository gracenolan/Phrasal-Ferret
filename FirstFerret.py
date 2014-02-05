#! /usr/bin/python3

import codecs
#import xml.etree.ElementTree as ET
from lxml import etree  # Lets use this as the xml parser, it has some more features :D
import sys
import fnmatch

# This is Phrasal Ferret's collection of phrases 
# dictionary of phrases with a count of how often they appear 
phrases = {}

# Phrasal Ferret needs to find some berries to eat. Will he find anything?
# He looks through the leaves (elements) to see what he can find
def print_all():
  root = tree.getroot()
  allChars = root.findall(".//*[@font]")
  for char in allChars:
    print(char.text)

#bold_phrase = ""
# method to find teh bold characters
font = "" # this holds the font tag so changes in font are detected
def find_bold(textline):
  bold_phrase = ""
  global font
  for text in textline:
    if not text.tag == "text":
      continue
    #print(text.text),
    if text.get("font"):
      if font == text.get("font"):  
        # Is this character part of a phrase we are already recording?
        # if this character is the same font as the last character
        # then append it to the current bold_phrase string
        bold_phrase += text.text 
        print(bold_phrase + "....")

      # if it is not the same, then see if the font is bold
      elif "Bold" in text.get("font"):
        # if this character is bold (the beginning of a phrase)
        # we need to save the old phrase
        # then add it to the bold_phrase. 
        # this will be the start of a new bold phrase
        # bold_phrase = text.text
        if len(bold_phrase) > 2: #if the phrase is actually holding something
          if not bold_phrase in phrases:
            # save last word
            print("saving ne word to phrases{}")
            phrases[bold_phrase] = 1
          else:
            print("incrementing " + bold_phrase + "in phrases{}")
            phrases[bold_phrase] += 1

        bold_phrase = text.text     # clear phrase and save beginning of new phrase
        font = text.get("font")
        print("Bold: " + text.text),
    # else try find italics ?
      else:
        continue

# Phrasal Ferret excitedly wiggles it's nose! It scuttles along the branches 
# in search for tasty text he can analyse. 
def find_text():
  root = tree.getroot()
  
  # are there leaves on this tree?
  if len(root):
    print("lets climb some branches!")
    
    # climb through the first branches
    for child in root:
      print(child.tag)

      # Get the textbox
      for textbox in child:
        if not textbox.tag == "textbox":
          continue
        print("  " + textbox.tag)

        # Get the textline
        for textline in textbox:
          if not textline.tag == "textline":
            continue
          print("    " + textline.tag)
          
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

print(phrases)
print("done")
raise SystemExit

