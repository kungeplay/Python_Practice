#!/usr/bin/python
#coding=utf-8
#检测一下是否发生了redirect动作,只要检查一下Response的URL和Request的URL是否一致就可以了.
import urllib2
import cookielib
my_url='http://www.google.cn'
response=urllib2.urlopen(my_url)
redirected=response.geturl()==my_url
print redirected

my_url='http://rrurl.cn/b1UZuP'
response=urllib2.urlopen(my_url)
redirected=response.geturl()==my_url
print redirected

#urllib2对Cookie的处理也是自动的。如果需要得到某个Cookie项的值，可以这么做
cookie=cookielib.CookieJar()
opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
response=opener.open('http://www.baidu.com')
print 'cookie值为:'
for item in cookie:
	print 'Name='+item.name
	print 'Value='+item.value
print 'HTTP的返回码为:',response.getcode()
