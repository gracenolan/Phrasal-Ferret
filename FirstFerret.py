#! /usr/bin/python3

import codecs
#import xml.etree.ElementTree as ET
from lxml import etree  # Lets use this as the xml parser, it has some more features :D
import sys
import fnmatch


# Phrasal Ferret needs to find some berries to eat. Will he find anything?
# He looks through the leaves (elements) to see what he can find
def smellingBerries():
  root = tree.getroot()
  allChars = root.findall(".//*[@font]")
  for char in allChars:
    print(char.text)


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
  smellingBerries()
else:
  print("Phrasel Ferret farts in your general direction.")

print("done?")
raise SystemExit

