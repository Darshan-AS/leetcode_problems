# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        
        head_a, head_b = headA, headB
        while head_a != head_b:
            head_a = headB if head_a is None else head_a.next
            head_b = headA if head_b is None else head_b.next
        
        return head_a
