"""Stock updating commands"""

import urllib2
import os

def update(stock):
  """grabs stock price, variable stock is a string \nfor the stock symbol you want info on"""
	url = 'http://finance.yahoo.com/q?s='
	try:
		t = urllib2.urlopen(url + stock).read()
	except:
		error = "invalid url"
		print error
		exit()
	place = t.find('<span class="time_rtq_ticker">')
	for i in range(place+31,len(t)):
		if (t[i:(i+1)] == '>'):
			block = i
			break
	for j in range(block+1,len(t)):
		if (t[j:(j+1)] == '<'):
			end = j
			break
	value = t[block+1:end]
	return {'price':value}


def base(stock):
  """grabs basic stock info, variable stock is a string \nfor stock symbol you want info on"""
	url = 'http://finance.yahoo.com/q?s='
	try:
		t = urllib2.urlopen(url + stock).read()
	except:
		error = "invalid url"
		print error
		exit()
	place = t.find('<span class="time_rtq_ticker">')
	for i in range(place+31,len(t)):
		if (t[i:(i+1)] == '>'):
			block = i
			break
	for j in range(block+1,len(t)):
		if (t[j:(j+1)] == '<'):
			end = j
			break
	value = t[block+1:end]
	place = t.find('<div class="title"><h2>')
	for k in range(place+23,len(t)):
		if (t[k:(k+1)] == "<"):
			end = k
			break
	name = t[place+23:end]
	place = t.find('Prev Close:</th><td class="yfnc_tabledata1">')
	for l in range(place+44,len(t)):
		if (t[l:(l+1)] == "<"):
			end = l
			break
	prev = t[place+44:end]
	place = t.find('Open:</th><td class="yfnc_tabledata1">')
	for m in range(place+38,len(t)):
		if (t[m:(m+1)] == "<"):
			end = m
			break
	open = t[place+38:end]
	return {'price':value,'name':name,'previous':prev,'open':open}
