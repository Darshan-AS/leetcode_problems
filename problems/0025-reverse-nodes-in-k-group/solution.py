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
        while j:
            count = 0
            while j and count < k:
                j = j.next
                count += 1
            
            if not j or count < k: break

            group, rest = i.next, j.next
            i.next = j.next = None

            r_group_head, r_group_tail = reverse(group), group
            i.next, r_group_tail.next = r_group_head, rest

            i = j = r_group_tail
        
        return sentinal_head.next
