def movies():
	import urllib2, os
	text = urllib2.urlopen("https://www.fandango.com/vancouver_wa_movietimes").read()
	start_16 = text.find('title="Theater Details and Box Office Info">Regal Cascade Stadium 16')
	t16_point = text.find('pos=Theater',start_16) + 11
	l = start_16
	y,x = 0,0
	movies = []
	time_16 = {}
	for i in range(0,9):
		l = text.find('name="&lid=MovieName&lpos=Theater' + str(text[t16_point:t16_point +1]) + '_MovieName">',l+46)
		end = text.find('</a>',l)
		if (end == -1 or l == -1):
			break
		movies.append(text[l+46:end].strip())
		p = l
		time_16[text[l+46:end].strip()] = []
		for j in range(0,16):
			p = text.find('<li class="timeWiredUnAvailable">',p+33)
			den = text.find('</li>',p)
			if (p == -1 or den == -1 or p > text.find('name="&lid=MovieName&lpos=Theater' + str(text[t16_point:t16_point +1]) + '_MovieName">',l+46)):
				p = text.find('<li class="timeWiredUnAvailable last">',l)
				den = text.find('</li>',p)
				time_16[text[l+46:end].strip()].append(text[p+38:den])
				break
			time_16[text[l+46:end].strip()].append(text[p+33:den])
	start_10 = text.find('title="Theater Details and Box Office Info">Regal Vancouver Plaza 10')
	t10_point = text.find('pos=Theater',start_10) + 11
	l = start_10
	party = []
	time_10 = {}
	for i in range(0,9):
		l = text.find('name="&lid=MovieName&lpos=Theater' + str(text[t10_point:t10_point +1]) + '_MovieName">',l+46)
		end = text.find('</a>',l)
		if (end == -1 or l == -1):
			break
		party.append(text[l+46:end].strip())
		p = l
		time_10[text[l+46:end].strip()] = []
		for j in range(0,16):
			p = text.find('<li class="timeWiredUnAvailable">',p+33)
			den = text.find('</li>',p)
			if (p == -1 or den == -1 or p > text.find('name="&lid=MovieName&lpos=Theater' + str(text[t10_point:t10_point +1]) + '_MovieName">',l+46)):
				p = text.find('<li class="timeWiredUnAvailable last">',l)
				den = text.find('</li>',p)
				time_10[text[l+46:end].strip()].append(text[p+38:den])
				break
			time_10[text[l+46:end].strip()].append(text[p+33:den])
	print '\n========regal 10=========\n========================='
	for j in party:
		print "\n" + j
		for i in time_10[j]:
			print i,
		print "\n"
	print '\n========regal 16=========\n========================='
	for j in movies:
		print "\n" + j
		for i in time_16[j]:
			print i,
		print "\n"
