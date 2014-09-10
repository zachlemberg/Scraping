#!/usr/bin/env python
#if you updated the github it updates some files, the ghetto way
scrap_files = ['youtube_check.py','read_hacks.py']#files from scraping project
#raw github url for the project code
scrap_url = "https://raw.githubusercontent.com/zachlemberg/Scraping/master/"
directory = '/home/example_user/scripts/' #where you want to put the files
#if you don't want to use the directory just put, directory = ''
#the files will be written in the same path where the github_update file is
from urllib2 import urlopen
for name in scrap_files:
	text = urlopen(scrap_url + name).read()
	f = open(directory + name,'w')
	f.write(text)
	f.close()
	print "updated " + name
