# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = head
        fast = head
        while True:
            if fast == None or fast.next == None:
                return False
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True