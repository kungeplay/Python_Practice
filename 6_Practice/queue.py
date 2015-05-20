#!/usr/bin/python
# coding=utf-8

#用列表实现一个简单的队列
query=[]

def pushit():
	query.append(raw_input("Enter new string:").strip())

def popit():
	if len(query)==0:
		print 'Cannot pop from an empty stack!'
	else:
		print 'Removed [',`query.pop(0)`,']'

def viewquery():
	print query

CMDS={'u':pushit,'o':popit,'v':viewquery}

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
				choice=raw_input(pr).strip().lower()[0]
			except (EOFError,KeyboardInterrupt,IndexError):
				choice='q'

			print '\nYou picked:[%s]' % choice

			if choice not in 'uovq':
				print 'Invalid option,try again'
			else:
				break

		if choice=='q':
					break
		else:				
			CMDS[choice]()

if __name__ == '__main__':
	showmenu()
