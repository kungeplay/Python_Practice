#!/usr/bin/python
# coding=utf-8
#这个文件的作用是测试一下命令行参数的使用方法
import sys

print 'you entered ',len(sys.argv),' arguments...' #len(sys.argv)是命令行参数的个数
print 'they were:',str(sys.argv) #sys.argv是命令行参数的列表
