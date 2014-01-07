# This Python file uses the following encoding: utf-8

import urllib2
from bs4 import BeautifulSoup

listfinal =file('listcut.txt','r')
i=1
book = str('chapter')
txt =str('.txt')

while 1:
	line = listfinal.readline()
	if not line:
		break
	i=i+1
 
	content = urllib2.urlopen(
	    #'file:///Users/AO/Desktop/7860218.html'
	    #'http://www.ranwen.net/files/article/18/18795/7851853.html'
	    line 
	    ).read()

	#print content
	
	soup = BeautifulSoup(content)
	soup=soup.find('div',id="content")
	#soup=soup.replace('<br/>','\n')

	#for i in soup:
		#i=i.replace('<br/>',"\n")
	 
	f = file('book.txt', 'w')
	f.write(soup.encode('utf-8'))
	f.close()
 
	fh = open('book.txt','r+')
	


	bookname = book + str(i) +txt
	i = int(i)
	out = file(bookname,'w')

	#print soup
	#f = file('book.txt', 'w')
	for j in fh.readlines():
	   	#i=i.replace('<br/>','\n')
	   	#out.write(j.replace('<div id="content" name="content">','\n'))
	   	#out.write(j.replace('<div align="center"><script src="/ssi/style-gg.js" type="text/javascript"></script></div>','\n'))

	   	out.write(j.replace('<br/>','\n'))
	   	#out.write(i.replace('<div/>','\n'))
	    #f.write(i.encode('utf-8')+'\n')

	fh.close()
	