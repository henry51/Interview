# -*- coding: utf-8 -*- 

#---------------------------------------  
#   程序：判断链表是否有环
#   来源：Baidu
#   作者：huangfs
#   日期：2016-04-07
#   语言：Python 3 
#   说明：Floyd's Algorithm (Tortoise and Hare Algorithm)
#   扩展：判断环起点位置 
#   参考：https://en.wikipedia.org/wiki/Cycle_detection#cite_note-9
#---------------------------------------

class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

# 判断是否有环(龟兔赛跑算法哈！)
def hasCycle(self, head):
	# type head : ListNode
	try:   #采用EAFP principle
		slow = head
		fast = head.next
		while slow != fast:
			slow = slow.next
			fast = fast.next.next   #利用快慢指针
		return True
	except:
		return False

# 判断环的起始位置
# 1.Floyd's Algorithm
def detectCycle(self, head):
	slow = fast = head
	while fast and fast.next:
		slow = slow.next
		fast = fast.next.next	
		if slow == fast:	# 判断有环之后的处理，核心在于慢指针的步数等于环长度的倍数
			slow = head
			while slow != fast:
				slow = slow.next
				fast = fast.next
			return slow
	return None

# 2. Brent's Algorithm
def detectCycle2(self, head):
	if (not head) or (not head.next) or (not head.next.next):
		return None
	slow = head
	fast = head.next
	power, period = 1, 1
	while slow != fast:
		if not fast:
			return None
		if power == period:
			slow = fast
			power = power * 2
			period = 0
		fast = fast.next
		period += 1
	slow = fast = head		#先寻找循环长度， 避免起点跟环起点相距过远，快指针在圈内多绕圈
	for _ in range(period):
		fast = fast.next
	while slow != fast:
		slow = slow.next
		fast = fast.next
	return slow
