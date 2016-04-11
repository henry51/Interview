# -*- coding: utf-8 -*- 

#---------------------------------------  
#   程序：求链表倒数第K个节点
#   来源：leetcode
#   作者：huangfs
#   日期：2016-04-11
#   语言：Python 3 
#---------------------------------------

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def theKthNode(head, k):
    #快慢双指针
    if k < 0:
        return None
    slow = fast = head
    for i in range(k):
        if fast:
            fast = fast.next
        else:
            return None
    while fast:
        slow = slow.next
        fast = fast.next
    return slow