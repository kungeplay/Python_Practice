#!/usr/bin/python
# coding=utf-8
#处理异常的一种方法,要注意的一点，except HTTPError 必须在第一个，否则except URLError将同样接受到HTTPError 。
#因为HTTPError是URLError的子类，如果URLError在前面它会捕捉到所有的URLError（包括HTTPError ）
#推荐使用urllie2_test09.py的异常处理方法
from urllib2 import Request,urlopen,URLError,HTTPError

req=Request('http://bbs.csdn.net/callmewhy')
try:
	response=urlopen(req)
except HTTPError,e:
	print 'The server couldn\'t fulfill the request.'
	print 'Error code:',e.code
except URLError,e:
	print 'we failed to reach a server.'
	print 'Reason:',e.reason
else:
	print 'No exception was raised.'

