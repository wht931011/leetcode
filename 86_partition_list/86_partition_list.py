# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        h1 = l1 = ListNode(0)
        h2 = l2 = ListNode(0)
        dummy = head
        while dummy!=None:
            if dummy.val<x:
                l1.next = dummy
                l1 = l1.next
            else:
                l2.next = dummy 
                l2 = l2.next
            dummy = dummy.next
        l2.next = None
        l1.next = h2.next
        return h1.next