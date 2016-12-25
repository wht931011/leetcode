# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = head
        while dummy!=None:
            while dummy.next!=None and dummy.val == dummy.next.val:
                dummy.next = dummy.next.next
            dummy = dummy.next
        return head