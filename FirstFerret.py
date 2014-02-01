#! /usr/bin/python3

import codecs
#import xml.etree.ElementTree as ET
from lxml import etree  # Lets use this as the xml parser, it has some more features :D
import sys
import fnmatch


# Phrasal Ferret needs to find some berries to eat. Will he find anything?
# He looks through the leaves (elements) to see what he can find
def print_all():
  root = tree.getroot()
  allChars = root.findall(".//*[@font]")
  for char in allChars:
    print(char.text)

  #print(etree.tostring(root, pretty_print = True))
  testing_char = root[0][0][0][0].get("font")
  print(testing_char)
  if "OCRB" in testing_char:
    print("YES this is a OCRB")

def find_bold():
  root = tree.getroot()
  # are there children? 
  if len(root):
    print("lets climb some branches")
    
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

          for text in textline:
            if not text.tag == "text":
              continue
            #print(text.text),
            if text.get("font"):
              if "Bold" in text.get("font"):
                print(text.text),


      if "textline" in child.tag:
        font = child[0].get("font")
        if "Bold" in font:
          print(font)
          bold_word.append(child[0].text)
      else:
        print("go down a branch")
  # look for textline tag
  # does the element contain "bold" ? 
  # does the next one contain "bold" ?
  # add them to string 
  # else go to the next textbox element 


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
  print_all()
  find_bold()
else:
  print("Phrasel Ferret farts in your general direction.")

print("done")
raise SystemExit

