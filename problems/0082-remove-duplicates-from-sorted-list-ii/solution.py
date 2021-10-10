# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = curr = ListNode(next=head)
        
        while curr and curr.next and curr.next.next:
            if curr.next.val == curr.next.next.val:
                val = curr.next.val
                while curr.next and curr.next.val == val:
                    curr.next = curr.next.next
            else:
                curr = curr.next
        
        return dummy_head.next
