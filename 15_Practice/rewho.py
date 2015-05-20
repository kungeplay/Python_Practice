#!/usr/bin/python
#coding=utf-8
from os import popen
from re import split
f=popen('who','r')
for eachline in f.readlines():
	print split('\s\s+|\t',eachline.strip())
f.close()