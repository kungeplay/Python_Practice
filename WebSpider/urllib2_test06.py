#!/usr/bin/python
#coding=utf-8
#URLError异常处理
import urllib2
req=urllib2.Request('http://www.baibai.com')#一个不存在的网址
try:
	urllib2.urlopen(req)
except	urllib2.URLError,e:
	print	e.reason
else:	#这一步不会执行
	print "NO error!"
