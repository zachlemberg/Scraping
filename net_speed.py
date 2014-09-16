#!/usr/bin/env python
#finds the apprioxamate speed of your network connection
from urllib2 import urlopen
import timeit
h = timeit.Timer("urlopen('http://www.google.com/')","from urllib2 import urlopen")
time = h.timeit(3) / 3 #gets the average of three attempts
info = urlopen("http://www.google.com/").read() #info transferred in bytes
amount_bits = len(info) * 8
speed = (amount_bits / time) * (1.0 / 1048576.0) # bits/seconds * (1 Kilobit/1024bits) * (1 Megabit/1024Kilobits)
print "your network speed is " + str(speed) + " Mb/s" #in megabits per second
