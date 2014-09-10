#!/usr/bin/env python
#check if there are new videos on the channels you like
#channels are added in the youtube config page
from urllib2 import urlopen
url = "http://www.youtube.com/user/"
#these are operations to read the channels from .youtube_config
try:
	t = open(".youtube_config").read()
	a = t.find("channels:")
	channels = (t[a+9:t.find("\n",a)]).split(",")
except:
	p = open(".youtube_config",'w')
	p.write("#begin config\nchannels:Collegehumor,Vsauce2\n#end config")
	p.write("\n-the channel names are dervived from url of youtube channel page")
	p.write("Example http://www.youtube.com/user/Collegehumor/featured")
	p.write("-add channel names in comma seperated list in continous line")
	p.close()
	t = open(".youtube_config").read()
	a = t.find("channels:")
	channels = (t[a+9:t.find("\n",a)]).split(",")
#i am using unix filesystem here, but windows users need to only add there file path here
file = ".channel_data" #local file stays with youtube_check.py
#this cactches error if the file was not made before the read
try:
	f = open(file).read()
except:
	b = open(file,'w')
	b.write("test write")
	b.close()
	f = open(file).read()
checking,i = True,0
data,fin_url = '',''
def find_1st_title(big_url):#grabs the first video title
	source = urlopen(big_url).read()
	index = source.find("yt-lockup-title")
	title_index = source.find('title="',index)
	title_end = source.find('" data',title_index+7)
	return source[title_index+7:title_end]
while checking:
	if i >= len(channels):
		break#stop checking if i have checked all the channels
	fin_url = url + channels[i] + "/videos"
	new_title = find_1st_title(fin_url)
	if channels[i] in f:
		index = f.find(channels[i])
		end = f.find("\n",index)
		old_title = f[index + len(channels[i]):end]
		if new_title == old_title:
			print "nothing new for " + channels[i]
		else:
			print "new videos " + channels[i] + " Newest is " + new_title
	else:
		print "channel added " + channels[i]
	data += channels[i] + new_title + "\n"
	i += 1
#again windows system paths or unix file paths are required here
finished_data = open(file,'w')
finished_data.write(data)
finished_data.close()
