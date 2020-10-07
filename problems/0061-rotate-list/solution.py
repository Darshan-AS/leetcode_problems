# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not k or not head: return head
        
        i = k
        a = b = head
        while i:
            if not b.next:
                b = head
                if not (i := k % (k - i + 1)): return head
                else: continue
            b = b.next
            i -= 1
        
        while b and b.next:
            a = a.next
            b = b.next
        
        new_head = a.next
        a.next = None
        b.next = head
        
        return new_head
