#!/usr/bin/env python
#stock values and stuff
import urllib2
#check my stock portfolio to check on my growth
moneyin = 0#global variable

def get_price(stock):
  #grabs stock price, variable stock is a string \nfor the stock symbol you want info on
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
	return value

def get_portfolio():
	url = "https://raw.githubusercontent.com/zachlemberg/Scraping/master/portfolio.txt"
	try:
		t = urllib2.urlopen(url).read()
	except:
		print "Error in reading portfolio file, oops"
		exit()
	lines = t.split('\n')
	stocks = []
	for line in lines:
		sym = line[0:line.find(' ')]
		shares = line[line.find(' '):]
		if (sym != "buy_price"):
			try:
				a = float(shares)
				stocks.append([sym,float(shares.strip())])
			except:
				pass#avoids errors, just doesnt write stock
		else:
			global moneyin
			moneyin = float(shares)
	return stocks

def parse_my_portfolio(data):
	worth = 0
	for stock in data:
		worth += float(get_price(stock[0]))*stock[1]
	return worth

#full system to get value
account = get_portfolio()
total_worth = parse_my_portfolio(account)
print "Total Portfolio: $" + str(total_worth)
print "Change in Value: "  +  str(float(int((total_worth - moneyin)*100))/100.0)
#Portfolio print out
print "Stock  Shares"
print "+++++++++++++"
for stock in account:
	print str(stock[0]) + " "*(8 - len(str(stock[0]))) + str(stock[1])
