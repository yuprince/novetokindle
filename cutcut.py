# This Python file uses the following encoding: utf-8
#这个函数是将list的herf链接拼接一个完整的链接传送给文本处理文件
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
 log = Log('listcut.txt', 'w+')

f =file('list.html','r')


relink = ' href="(.*)"'
#info = '<a href="http://www.baidu.com">baidu</a>'
#info = '<td><div class="dccss"><a alt="第三章 夜深（今天三更完成，求收藏推荐）" href="5746690.html">第三章 夜深（今天三更完成，求收藏推荐）</a></div></td>'
listhead = 'http://www.ranwen.net/files/article/18/18795/'

while 1:
	while 1:
		line = f.readline()
		if not line:
			break
		pass

		info = line

		cinfo = re.findall(relink,info)
		if len(cinfo) == 0:
			break

		cinfostr= cinfo[0]
		#cinfostr = cinfo
		if cinfostr == []: 
			break
		listend = str(cinfostr)
		listfianl = listhead + listend

		
		print listfianl
	if not line:
			break
'''
cinfo = re.findall(relink,info)
cinfo=str(cinfo).encode('utf-8')

print cinfo
'''
'''
relink = '<a href="(.*)">(.*)</a>'
info = '<a href="http://www.baidu.com">baidu</a>'
cinfo = re.findall(relink,info)
print cinfo
'''