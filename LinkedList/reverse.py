# -*- coding: utf-8 -*- 

#---------------------------------------  
#   程序：反转单向链表
#   来源：bytedance
#   作者：huangfs
#   日期：2016-04-11
#   语言：Python 3 
#---------------------------------------

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# method 1. three temp point  iterative
def reverse1(head):
    if head == None or head.next == None:
        return head
    p1 = head
    p2 = head.next
    while p2:
        p3 = p2.next
        p2.next = p1
        p1 = p2
        p2 = p3
    head.next = None
    return p1

# method 2. two temp point  iterative   insert node after head one by one and handle head node at last.
def reverse2(head):
    p = head.next
    while p.next:
        q = p.next
        p.next = q.next
        q.next = head.next
        head.next = q
    p.next = head
    head = p.next.next
    p.next.next = None
    return head

# method 3. recursive 
def reverse3(head):
    p = head
    if p == None:
        return None
    q = head.next
    if q == None:
        return p
    head = reverse3(q)
    q.next = p
    p.next = None
    return head
