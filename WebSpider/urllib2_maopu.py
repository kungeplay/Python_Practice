#!/usr/bin/python
#coding=utf-8
import sys
import urllib
import urllib2
import re


def OpenPage(url):
	'打开页面，返回页面内容'
	print '地址为: ',unicode(url)
	sys.stdout.flush()
	user_agent='Mozilla/5.0 (X11; Linux x86_64; rv:31.0) Gecko/20100101 Firefox/31.0'
	headers={'User-Agent':user_agent}
	req=urllib2.Request(url,headers=headers)
	myResponse=urllib2.urlopen(req)
	return myResponse.read()

def ReadFile(filename):
	'读取文件，返回文件内容'
	f=open(filename,'r')	#r以读方式打开,r+以读写模式打开
	filecontent=f.read()
	f.close()
	return filecontent

def WriteFile(filename,message):
	
	f=open(filename,'w')
	f.write(message)
	f.close()

def PageCount(mypage):
	'统计这个贴吧中的页数'
	countcompile=re.compile(r'<a style="cursor: pointer;" class="m-page-i fl" href=".+?" rel="\d+?">(\d+?)</a>\W*?<a style="cursor: pointer;" class="m-page-down fl" href=".+?" rel="\d">下一页</a>',re.S)
	countreg=countcompile.search(mypage)
	if countreg is not None:
		return countreg.group(1)
	else:
		return ''

def GetCurrentPageNum(mypage):
	'获取当前页面的页数'
	currentcompile=re.compile(r'<a style="cursor: pointer;" class="m-page-i fl on" href=".+?" rel="\d+?">(\d+?)</a>',re.S)
	currentnum=currentcompile.search(mypage)
	if currentnum is not None:
		return currentnum.group(1)
	else:
		return ''	

def GetTitle(mypage):
	'获取帖子的标题'
	titlecompile=re.compile(r'<h1 class="c333 subTitle" style="color: .+?" >(.+?)</h1>',re.S)
	title=titlecompile.search(mypage)
	if title is not None:
		return title.group(1)
	else:
		return ''


def GetNextPageUrl(mypage):
	'获取下一页的地址'		
	nexturlcompile=re.compile(r'<a style="cursor: pointer;" class="m-page-down fl" href="(.+?)" rel="\d+?">下一页</a>',re.S)
	nexturlreg=nexturlcompile.search(mypage)
	if nexturlreg is not None:
		nexturl=re.sub(r'\s','',nexturlreg.group(1).strip())
		if nexturl[0]=='/':
			nexturl='http://dzh.mop.com'+nexturl
		return nexturl	
	else:
		return ''

def GetMess(page):
	'提取页面中楼主发言'
	message=''	#提取出的页面内容
	messcompile=re.compile(r'<div class="article-cont p20 c666">(.*?)</div>|<div class="mt10 inner-txt fs14 mt15 lh22">(.*?)</div>',re.S)
	messreg=messcompile.findall(page)
	if messreg:		#一个空list本身等于False
		for eachcontent in messreg:
			if eachcontent[0]:
				result=re.sub(r'<p>|</p>|<span.*?>|</span>','',eachcontent[0])
				result=re.sub(r'<br />','',result)
			else:
				result=re.sub(r'<p>|</p>|<span.*?>|</span>|&nbsp;','',eachcontent[1])
				result=re.sub(r'<br />|<br>|<	/br>','',result)				
			message+= result

	return message
	




def main():

	#yurl='http://dzh.mop.com/47958053_1.html?from=3&Stop=0&SKind=1&master=1#reply-begin'
	myurl="http://dzh.mop.com/47504930_1.html?from=3&Stop=96&SKind=1&Stop=96&SKind=1&master=1#reply-begin"
	mypage=OpenPage(myurl)


	mytitle=GetTitle(mypage)
	if mytitle !='':
		print  '标题:',mytitle
		sys.stdout.flush()

	mypagecount=PageCount(mypage)
	if mypagecount !='':
		print '页数: ',mypagecount
		sys.stdout.flush()

	
	mycurrentpagenum=GetCurrentPageNum(mypage)	
	while mycurrentpagenum!='' and mycurrentpagenum<= mypagecount:
		filename=mytitle+'----'+mycurrentpagenum+'.txt'
		print '正在下载:%s' %(filename)
		sys.stdout.flush()
		WriteFile(filename,GetMess(mypage))

		myurl=GetNextPageUrl(mypage)
		
		if myurl=='':
			break

		else:	
			mypage=OpenPage(myurl)
			mycurrentpagenum=GetCurrentPageNum(mypage)

	print 'It is over!'	



if __name__ == '__main__':
	main()



