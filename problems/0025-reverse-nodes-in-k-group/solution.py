# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head_: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(head: Optional[ListNode]) -> Optional[ListNode]:
            i, j = None, head
            while j:
                j.next, i, j = i, j, j.next
            
            return i
        
        sentinal_head = i = j = ListNode(next=head_)
        while j and j.next:
            count = 0
            while j and j.next and count != k:
                j = j.next
                count += 1
                        
            if count == k:
                j_next = j.next
                j.next = None
                j = i.next
                i.next = reverse(i.next)
                j.next = j_next
            
            i = j
        
        return sentinal_head.next
