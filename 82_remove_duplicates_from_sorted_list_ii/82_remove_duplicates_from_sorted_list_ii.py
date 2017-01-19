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
        dummy = ListNode(0)
        dummy.next = head
        curr = head
        pre = dummy
        while curr != None:
            while curr.next != None and curr.val == curr.next.val:
                curr = curr.next
            if pre.next == curr:
                pre = pre.next
            else:
                pre.next = curr.next
            
            curr = curr.next
                
                
        return dummy.next
                
                
        