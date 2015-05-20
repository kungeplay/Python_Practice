#!/usr/bin/python
#coding=utf-8
# 这段代码练习使用一些os和os.path模块中的功能。它创建一个文本文件，写入少量数据，然后重命名，输出文件内容。同时还进行了一些辅助性的文件操作，比如遍历目录树和文件路径名处理。
import os

for tmpdir in ('/tmp',r'c:\temp'):
	if os.path.isdir(tmpdir):
		break
else:
	print 'no temp directory available!'
	tmpdir=''

if tmpdir:
	os.chdir(tmpdir)
	cwd=os.getcwd()
	print '***current temporary directory'
	print cwd

	print '***creating example directory...'

	os.mkdir('example')
	os.chdir('example')
	cwd=os.getcwd()
	print '***new working directory:'
	print cwd
	print '***original directory listing:'
	print os.listdir(cwd)

	print '***creating test file'
	fobj=open('test','w')
	fobj.write('foo\n')
	fobj.write('bar\n')
	fobj.close()
	print '***updated directory listing:'
	print os.listdir(cwd)

	print "***renaming 'test' to 'filetest.txt'"
	os.rename('test','filetest.txt')
	print '***updated directory listing:'
	print os.listdir(cwd)

	path=os.path.join(cwd,os.listdir(cwd)[0])
	print '***full file pathname'
	print path
	print '***(pathname,basename)=='
	print os.path.split(path)
	print '***(filename,extension)=='
	print os.path.splitext(os.path.basename(path))

	print '***displaying file contents:'
	fobj=open(path)
	for eachLine in fobj:
		print eachLine,
	fobj.close()


print '***deleting test file'
os.remove(path)
print 'updated directory listing:'
print os.listdir(cwd)
os.chdir(os.pardir)
print '***deleting test directory'
os.rmdir('example')
print '***DONE'



