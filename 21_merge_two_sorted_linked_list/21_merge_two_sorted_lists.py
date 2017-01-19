# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        newhead = dummy = ListNode(0)
        curr1 = l1
        curr2 = l2
        while curr1 != None and curr2 != None:
            if curr1.val < curr2.val:
                dummy.next = curr1
                curr1 = curr1.next
            else:
                dummy.next = curr2
                curr2 = curr2.next
            dummy = dummy.next
        if curr1 == None:
            dummy.next = curr2
        if curr2 == None:
            dummy.next = curr1
        return newhead.next
                