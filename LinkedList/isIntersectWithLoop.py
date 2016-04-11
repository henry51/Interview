# -*- coding: utf-8 -*- 

#---------------------------------------  
#   程序：求两单向有环链表是否相交
#   来源：<编程之美>
#   作者：huangfs
#   日期：2016-04-11
#   语言：Python 3 
#---------------------------------------

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def isIntersectWithLoop(h1, h2):
	# 利用单链表判断有环的方法先求得环内相交点
	slow = fast = h1;
    while(fast and slow)
    {
        fast = fast.next.next
        slow = slow.next;
        if(fast == slow)
        {
            circleNode1 = fast;
            break
        }
    }
    slow = fast = h2;
    while(fast and slow)
    {
        fast = fast.next.next
        slow = slow.next;
        if(fast == slow)
        {
            circleNode2 = fast;
            break
        }
    }
    #若两链表相交，则共有一个环，即环上任意一节点都在两个链表中
    temp = circleNode2.next
    while temp != circleNode2:
    	if temp = circleNode1:
    		return True
    	temp = temp.next
    return False 
