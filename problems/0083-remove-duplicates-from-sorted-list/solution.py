# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = ListNode(next=head)
        val = float('inf')
        
        while curr and curr.next:
            if curr.next.val == val:
                curr.next = curr.next.next
            else:
                val = curr.next.val
                curr = curr.next
        
        return head
