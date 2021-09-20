# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy_head = i = j = ListNode(next=head)
        
        for _ in range(n):
            j = j.next
        
        while j and j.next:
            i, j = i.next, j.next
        
        i.next = i.next.next
        return dummy_head.next
