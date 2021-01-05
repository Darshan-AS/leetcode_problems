# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = curr = ListNode(-1)
        while l1 and l2:
            low, high = (l1, l2) if l1.val < l2.val else (l2, l1)
            curr.next = low
            curr = curr.next
            l1, l2 = (l1.next, l2) if l1 == low else (l1, l2.next)
        curr.next = l1 if l1 else l2
        return head.next
