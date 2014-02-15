#! /usr/bin/python3

# This is Using a library created by Christopher Beckham 

from cz import cz

import sys


# Search for artcles in Google Scholar
def search(query):
  url = 'http://scholar.google.co.nz/scholar?q=' + query.replace(" ", "+") + '&btnG=&hl=en&as_sdt=0%2C5'
  body = cz.geturl(url, agent='Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1667.0 Safari/537.36')
  elems = cz.getbetween(body, '<a href="/scholar?cites=', '">')

  new_url = 'http://scholar.google.co.nz/scholar?cites=' + elems[0]
  print ("Citations url:  " + new_url)

  body = cz.geturl(new_url)
  elems = cz.getbetween(body, '<h3 class="gs_rt"><a href="', '"')

  for elem in elems:
    print (elem)

if __name__ == "__main__":
  if len(sys.argv) >= 1:
    query = sys.argv[1]
    print ("Our query is:  " + query)
    search(query)
  else:
    print("Please enter the name of the article and the most common phrase")
    raise SystemExit




