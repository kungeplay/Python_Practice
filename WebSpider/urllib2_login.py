#!/usr/bin/python
#coding=utf-8
import urllib
import urllib2
postdata=urllib.urlencode({
	'username':'坤哥玩电驴',
	'passowrd':'132133',
	'continue':'http://www.verycd.com/',
	'fk':'',
	'login_submit':'登录'
})
headers={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:31.0) Gecko/20100101 Firefox/31.0'}
req=urllib2.Request(
	url='http://secure.verycd.com/signin?error_code=emptyInput&amp;continue=http://www.verycd.com/',
	data=postdata,
	headers=headers
)
result=urllib2.urlopen(req)
print result.code
result2=urllib2.urlopen('http://www.verycd.com/')
print result2.read()
