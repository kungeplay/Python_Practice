#!/usr/bin/python
#coding=utf-8
#查看HTTP应答对象response包含的状态码
import urllib2
req=urllib2.Request('http://bbs.csdn.net/callmewhy')

try:
	urllib2.urlopen(req)

except urllib2.URLError,e:
	print e.code