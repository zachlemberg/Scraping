#!/usr/bin/env python
#grabs age on a famous person
#this is a script not a maintained definition for future use
from urllib2 import urlopen
url = "http://en.wikipedia.org/wiki/"
asking = True
print "whose age would you like to know?"
while asking == True:#loop to ask for a name
	name = raw_input()#ask for a name
	list = name.split(' ')
	if len(list) == 2:#if there is a name and lastname
		asking = False
	else:#ask more specifically
		print "please specify a surname and name with a space"
Clist = []
for i in [0,1]:#capitalize name and last name
	Clist.append(list[i].capitalize())
celeb_name = "_".join(Clist)
url += celeb_name
try:#load wiki page
	html = urlopen(url).read()
	error = 0
except:#if page doesn't exist on wiki
	print "couldn't find celeb"
	error = 1
if error == 0:
	index = html.find('ForceAgeToShow">(age&#160;')
	if (index != -1): #if page exist and there is an age on page
		endex = html.find(')</span>',index)#finds character after age
		answer = html[index + 26:endex]#just age
		print answer
	else:	print "couldn't find that persons age"
