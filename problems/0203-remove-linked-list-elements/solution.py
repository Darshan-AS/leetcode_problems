# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        start = i = ListNode(0)
        i.next = head
        while i and i.next:
            if i.next.val == val:
                i.next = i.next.next
            else:
                i = i.next
            
        return start.next
