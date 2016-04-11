# -*- coding: utf-8 -*- 

#---------------------------------------  
#   程序：求链表的中间节点
#   来源：<编程之美>
#   作者：huangfs
#   日期：2016-04-11
#   语言：Python 3 
#---------------------------------------

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def theMiddleNode(head):
	# 同快慢指针概念，只是这次快指针每次移动都快一步
	if head == None or head.next == None:
		return head
	slow = fast = head
	while(fast and fast.next):
		fast = fast.next.next
		slow = slow.next
	return slow
