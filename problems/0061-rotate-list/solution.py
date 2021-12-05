# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: return head
        dummy_head = a = b = curr = ListNode(next=head)
        
        n = 0
        while curr and curr.next:
            curr = curr.next
            n += 1
        
        for _ in range(k % n):
            b = b.next
        
        while b and b.next:
            a, b = a.next, b.next
        
        b.next = dummy_head.next
        dummy_head.next = a.next
        a.next = None
        
        return dummy_head.next
