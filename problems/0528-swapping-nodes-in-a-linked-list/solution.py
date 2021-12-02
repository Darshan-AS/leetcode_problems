# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy_head = i = j = ListNode(next=head)
        k_begin = k_end = None
        
        for _ in range(k - 1):
            j = j.next
        k_begin = j
        j = j.next
        
        while j and j.next:
            i, j = i.next, j.next
        k_end = i
        
        a, b = k_begin.next, k_end.next
        k_begin.next, k_end.next = b, a
        a.next, b.next = b.next, a.next
        
        return dummy_head.next
