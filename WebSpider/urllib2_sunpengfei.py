#!/usr/bin/python
#coding=utf-8
import urllib
import urllib2
postdata=urllib.urlencode({
	'uid_mail':'坤哥玩电驴',
	'passowrd':'132133',
	'continue':'http://www.verycd.com/',
	'fk':'',
	'login_submit':'登录'
})
headers={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:31.0) Gecko/20100101 Firefox/31.0'}
req=urllib2.Request(
	url='http://192.168.2.106:8000/chat/loginValidate',
	#data=postdata,
	headers=headers
)
result=urllib2.urlopen(req)
print result.read()
