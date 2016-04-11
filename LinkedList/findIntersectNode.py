# -*- coding: utf-8 -*- 

#---------------------------------------  
#   程序：求两单向无环链表相交的第一个公共点
#   来源：<编程之美>
#   作者：huangfs
#   日期：2016-04-11
#   语言：Python 3 
#---------------------------------------
 from LinkedListCycle import detectCycle
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def findIntersectNode(h1, h2):
	# 人为构造环
	temp = h1
	while temp.next:
		temp = temp.next
	temp.next = h2
	detectCycle(h1)

	#也可以通过计算链表的长度差来调整指针出发时刻，从而得到相交点
