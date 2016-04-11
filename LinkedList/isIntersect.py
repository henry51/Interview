# -*- coding: utf-8 -*- 

#---------------------------------------  
#   程序：求两单向无环链表是否相交
#   来源：<编程之美>
#   作者：huangfs
#   日期：2016-04-11
#   语言：Python 3 
#---------------------------------------

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def isIntersect(h1, h2):
    #考虑若相交，必有链表的公共节点， 复杂度为O(m+n)
    if h1 == None or h2 == None:
        return None
    while (h1.next):
        h1 = h1.next
    while (h2.next):
        h2 = h2.next
    return h1 == h2