#!/usr/bin/env python
#find hackaday headlines, no metadata support
from urllib2 import urlopen
text = urlopen("http://hackaday.com/").read()
head_index = []
arti_index = []
url_index = []
urls = []
titles = []
info = []
rando = 0
next = 0
def subhtml(text): #subtract html from text
	r = 0
	while r != -1:
		r = text.find('<')
		if r != -1:
			n = text.find('>')
			text = text[0:r] + text[n+1:]
	return text
def substuff(text): #subtracts stupid &nbsp; or &#8212;
	r = 0
	while r != -1:
		r = text.find('&')
		if r != -1:
			n = text.find(';',r)
			text = text[0:r] + text[n+1:]
	return text
while next != -1:
	next = text.find('<h2 class="entry-title">',next+1)
	if next != -1:
		head_index.append(next)
		url_index.append(text.find('<a href="',next))
for num in head_index:
	rando = text.find('</h2>',num)
	titles.append(substuff(subhtml(text[num:rando])))
for t in url_index:
	rando = text.find('/"',t)
	urls.append(text[t+9:rando+1])
next = 0
while next != -1:
	next = text.find('<div class="entry-content">',next+1)
	if next != -1:
		arti_index.append(next)
for start in arti_index:
	rando = text.find('</div>',start)
	info.append(substuff(subhtml(text[start:rando])))
for i in range(0,len(head_index)):
	print titles[i]
	print info[i]
	print "URL: " + urls[i]
	print "------------"
	print " "
