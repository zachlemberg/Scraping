#!/usr/bin/env python
#if you updated the github it updates some files, the ghetto way
scrap_files = ['youtube_check.py','read_hacks.py']#files from scraping project
#raw github url for the project code
scrap_url = "https://raw.githubusercontent.com/zachlemberg/Scraping/master/"
directory = '/home/zlemberg/scripts/' #where you want to put the files
from urllib2 import urlopen
for name in scrap_files:
	text = urlopen(scrap_url + name).read()
	f = open(directory + name,'w')
	f.write(text)
	f.close()
	print "updated " + name
