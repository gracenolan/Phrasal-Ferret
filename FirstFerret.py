#! /usr/bin/python

import codecs
import xml.etree.ElementTree as ET
import sys
import fnmatch

# Read in the file name
if len(sys.argv) != 2:
  print "Usage: FirstFerret.py <xml file> \nPhrasel Ferret likes to climb xml trees. They have the softest leaves and pleasant smelling flowers. Please try again with an xml file >^_^<"
  raise SystemExit
elif fnmatch.fnmatch(sys.argv[1], "*.xml"): 
  filename = sys.argv[1]
  tree = ET.parse(codecs.open(filename, encoding = "UTF-8")) # build tree
  smellingBerries(tree)
else:
  print "Phrasel Ferret farts in your general direction"

# test structure 
def smellingBerries(ET):
  root = tree.getroot()
  allChars = root.findall(".//*[@font]")
  for char in allChars:
    print char.text

print "done?"

raise SystemExit

