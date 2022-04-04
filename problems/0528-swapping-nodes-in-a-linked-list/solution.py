# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        sentinal_head = i = j = ListNode(next=head)
        k_begin = k_end = None
        
        for _ in range(k - 1):
            j = j.next
        k_begin = j
        
        j = j.next
        while j and j.next:
            i, j = i.next, j.next
        k_end = i
        
        b, e = k_begin.next, k_end.next
        k_begin.next, k_end.next = e, b
        b.next, e.next = e.next, b.next
        
        return sentinal_head.next
