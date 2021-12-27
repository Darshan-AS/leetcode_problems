# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseEvenLengthGroups(self, head_: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(head: Optional[ListNode]) -> Optional[ListNode]:
            i, j = None, head
            while j:
                j.next, i, j = i, j, j.next
            
            return i
        
        sentinal_head = i = j = ListNode(next=head_)
        group = 1
        while j and j.next:
            count = 0
            while j and j.next and count != group:
                j = j.next
                count += 1
                        
            if count % 2 == 0:
                j_next = j.next
                j.next = None
                j = i.next
                i.next = reverse(i.next)
                j.next = j_next
            
            group += 1
            i = j
        
        return sentinal_head.next
