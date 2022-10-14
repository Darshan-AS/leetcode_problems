# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: ListNode | None) -> ListNode | None:
        walker = runner = sentinel_head = ListNode(next=head)
        
        while runner.next and runner.next.next:
            walker = walker.next
            runner = runner.next.next
            
        walker.next = walker.next.next
        return sentinel_head.next
