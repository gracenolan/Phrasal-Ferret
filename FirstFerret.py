#! /usr/bin/python

import xml.etree.ElementTree as ET
import sys

# Read in the file name
filename = sys.stdin.readlines()
if filename != "*.xml" :
  print "Phrasel Ferret likes to climb xml trees only. They have the softest leaves and pleasant smelling flowers. Please try again with an xml file >^_^<"
else if filename == null:
  print "Usage: FirstFerret.py <xml file> "
else tree = ET.parse(filename) # build tree 
root = tree.getroot()

# test structure 
for child in root:
  print child.tag, child.attrib

