#!/usr/bin/python
#! coding=utf-8
#默认函数对象参数举例
#这段脚本下载了一个web页面，并显示了HTML文件的第一个以及最后一个非空行。process()函数可以做我们想要的任何事，
from urllib import urlretrieve

def firstNonBlank(lines):
	for eachLine in lines:
		if not eachLine.strip():
			continue
		else:
			return eachLine
	if not eachLine.strip():
		return 'No Pages'

def firstLast(webpage):
	f=open(webpage)
	lines=f.readlines()
	f.close()
	print firstNonBlank(lines),
	lines.reverse()
	print firstNonBlank(lines),

def download(url='http://www.sina.com.cn',process=firstLast):
	try:
		retval=urlretrieve(url)[0]
	except IOError:
		retval=None
	if retval: #do some processing
		print 'the download file: ',retval
		process(retval)
	else:
		print 'retval wrong!'	

if __name__ == '__main__':
			download()		
