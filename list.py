# This Python file uses the following encoding: utf-8

import urllib2
from bs4 import BeautifulSoup
import re
import sys
class Log(object):
 def __init__(self, *args):
  self.f = file(*args)
  sys.stdout = self
  
 def write(self, data):
  self.f.write(data)
  sys.__stdout__.write(data)
  
if __name__ == '__main__': 
 log = Log('list.html', 'w')

def has_class_dccss_but_not_other_herf(tag):
	return tag.has_attr('class') and not tag.has_attr('id') 
 
content = urllib2.urlopen('file:///Users/AO/Desktop/index.html').read()


 
soup = BeautifulSoup(content)

soup = soup.find_all(has_class_dccss_but_not_other_herf)
print soup

filex = file('list.html','r')
endmark=('</td>, <div class="dccss"><a alt="第一章 燃烧的火刑架"')
while 1:
	line = filex.readline()
	if not line:
		break
	if re.match(endmark,line) !='none':
		break
	print line

