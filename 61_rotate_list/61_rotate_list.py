# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None: return None
        dummy = head
        size = 1
        while dummy.next != None:
            size += 1
            dummy = dummy.next
        dummy.next = head
        count = size - k % size
        while count > 0:
            dummy = dummy.next
            count -= 1
        head = dummy.next
        dummy.next = None
        return head
        