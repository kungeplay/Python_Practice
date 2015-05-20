#!/usr/bin/python
#coding=utf-8
#参数组举例
#一个儿童游戏，可以随机选择算术加减法。我们通过函数add(),sub()等价+-操作符，这两者都可以在operator模块中找到。接着我们生成一个参数列表(该列表只有2个参数，因为这些是二元操作符/运算).接着选择任意的数字作为算子。因为我们没打算在这个程序的基础版本中支持负数，所以我们将两个数字的列表按从大到小的顺序排序，然后用这个参数列表和随机选择的算术操作符去调用相对应的函数，最后获得问题的正确答案。
#随机选择数字以及一个算术函数。显示问题，以及验证结果。在3次错误的尝试后给出答案。等到用户输入一个正确的答案后便会继续运行
from operator import add,sub
from random import randint,choice

ops={'+':add,'-':sub}
MAXTRIES=2

def doprob():
	op=choice('+-')
	nums=[randint(1,10) for i in range(2)]
	nums.sort(reverse=True)
	ans=ops[op](*nums)
	pr='%d %s %d=' %(nums[0],op,nums[1])
	oops=0
	while True:
		try:
			if int(raw_input(pr))==ans:
				print 'correct'
				break
			if oops==MAXTRIES:
				print 'answer\n%s%d'%(pr,ans)
			else:
				print 'incorrect...try again'
				oops+=1
		except (KeyboardInterrupt,EOFError,ValueError), e:
			print 'invalid input... try again'


def main():
	while True:
		doprob()
		try:
			opt=raw_input('Again?[y]').lower()
			if opt and opt[0]=='n':
				break
		except (KeyboardInterrupt,EOFError),e:
			print
			break		

if __name__ == '__main__':
				main()			
