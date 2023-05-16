# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        sentinal = h = ListNode(next=head)

        while h and (p := h.next) and (q := h.next.next):
            h.next, q.next, p.next, h = q, p, q.next, p
        
        return sentinal.next
