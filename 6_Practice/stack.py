#!/usr/bin/python
# coding=utf-8

#用列表模拟堆栈,编码命令也可以这样，放在第一或第二行# -*- coding: utf-8 -*-

stack=[]

def pushit():
	stack.append(raw_input('Enter New string: ').strip())

def popit():
	if len(stack)==0:
		print 'Cannot pop from an empty stack!'
	else:
		print 'Removed [',`stack.pop()`,']'

def viewstack():
	print stack #calls str() internally

CMDS={'u':pushit,'o':popit,'v':viewstack}

def showmenu():
	pr="""
	p(U)sh
	p(O)p
	(V)iew
	(Q)uit

	Enter choice:"""

	while True:
		while True:			
			try:
				choice=raw_input(pr).strip()[0].lower()
			except (EOFError,KeyboardInterrupt,IndexError): # 输入^D(EOF,产生一个EOF错误)，或者^C(中断退出，产生一个KeyboardInterrupt异常)
				choice='q'

			print '\nYou picked" [%s]' % choice
			if choice not in 'uovq':
					print 'Invalid option,try again'
			else:
				break	

		if choice=='q':
			break

		CMDS[choice]()

if __name__ == '__main__':
	showmenu()

