PHRASAL FERRET welcomes you to its humble abode! 

Phrasal Ferret looks for phrases in academic documents.
It finds the phrases that are in Bold. Then it sees how many times these phrases appear.

Before you ask Phrasal Ferret to find those phrases, you need to have the document
you want to scan extracted to xml format. pdf2txt.py (a program some other dude 
wrote) can extract text as xml from pdf documents.

I have included a document I've used as test data. This is called 3vs.xml

To unlesh Phrasal Ferret, run the follow in commandline:
$ python FirstFerret.py 3vs.xml 

Currently Phrasal Ferret will print out the document, then at the bottom say how many 
phrases it has found and which one is the most common. 
The count here isn't accurate as it is only counting the first occurance of the phrase.
I am currently working on making it count how often those phrase appear.
