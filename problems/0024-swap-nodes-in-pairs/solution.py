# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sentinal_head = h = ListNode(next=head)
        
        while h and h.next and h.next.next:
            p, q = h.next, h.next.next
            h.next, q.next, p.next = q, p, q.next
            h = h.next.next
        
        return sentinal_head.next
