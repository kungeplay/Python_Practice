#!/usr/bin/python
# coding=utf-8
#发送data表单数据
import urllib
import urllib2

url='http://mail.126.com'
values={'username':'blueskywwww','password':'sqfj2005'}
data=urllib.urlencode(values)	#编码工作
req=urllib2.Request(url,data)	#发送请求同时传data表单
response=urllib2.urlopen(req)	#请求反馈的信息
the_page=response.read()	#读取反馈的内容
print the_page
