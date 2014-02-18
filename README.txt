
----This is Phrasal Ferret!----

The purpose of Phrasal Ferret is to research the identification of new formalistions.
It was created as a summer research project under the University of Waikato.
Supervisor: Dr Craig Schock.

Phrasal Ferret looks for the most common phrase in an academic document.
It finds the phrases that are italised. Then it sees how many times these phrases appear.
This is to try and search for what is possibily a new formalisation.

Before you ask Phrasal Ferret to find those phrases, you need to have the document
you want to scan extracted to xml format.

PLEASE USE pdf2txt.py to extract text as xml from pdf documents.
I have hard coded to read the xml structure pdf2txt outputs.
I have included a document I've used as test data. This is called ff_med.xml

To give Phrasal Ferret a test run, put the following in commandline:
$ python PhrasalFerret.py ff_med.xml 

It will tell you the most common phrase, how often it appears and the title of the document.
The program will ask you if you would like to search for this in Google Scholar.
Please use this option sparingly!
Google doesn't exactly like it when their websites are scraped for data...
This option will return the top ten results for related documents.


