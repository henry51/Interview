# -*- coding: utf-8 -*- 

#---------------------------------------  
#   程序：删除链表中任意一个节点
#   来源：<编程之美>
#   作者：huangfs
#   日期：2016-04-11
#   语言：Python 3 
#---------------------------------------

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def deleteRandomNode(node):
	#要求O(n)时间复杂度，所以本质是需要改变链表，缺陷是无法针对最后一个节点这么做。
	node.val = node.next.val
	node.next = node.next.next

