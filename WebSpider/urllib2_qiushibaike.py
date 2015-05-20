#!/usr/bin/python
#coding=utf-8
import urllib
import urllib2
import re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
request=urllib2.Request('http://www.qiushibaike.com/hot/page/1')
request.add_header('User-Agent','Mozilla/5.0 (X11; Linux x86_64; rv:31.0) Gecko/20100101 Firefox/31.0')
response=urllib2.urlopen(request)
resstr=response.read()
#print 'response code: ',response.code
pattern=re.compile(r'<div class="content" title=".+?">(.+?)</div>',re.S)
matchstr=pattern.findall(unicode(resstr))
if matchstr is not None:
	print 'matchstr=',len(matchstr)
	for eachmatch in matchstr:
		print eachmatch.strip()
	#print matchstr.group(1).strip()
else:
	print 'No match!'

