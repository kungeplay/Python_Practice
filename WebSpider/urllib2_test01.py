#!/usr/bin/python
# coding=utf-8
##在Python中，我们使用urllib2这个组件来抓取网页。
##urllib2是Python的一个获取URLs的组件。
##它以urlopen函数的形式提供了一个非常简单的接口。
##注意urllib2和urllib并不是可以相互代替的。
import urllib2
response=urllib2.urlopen('http://www.baidu.com/')
#html=response.readline()#readline()是读取一行
html=response.read()
print html.decode('utf-8')
