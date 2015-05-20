#!/usr/bin/python
# coding=utf-8
#测试一下看看当使用输入方法如read()或者readlines()从文件中读取行时，Python并不会删除行结束符

f=open('test.txt','r')
data=[line.strip()for line in f.readlines()] #strip()函数删去了行结束符'\n'
f.close()
print data
a="你好"
print a

