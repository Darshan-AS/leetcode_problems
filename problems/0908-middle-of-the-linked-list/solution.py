# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        walker = runner = head
        while runner and runner.next:
            walker = walker.next
            runner = runner.next.next
        return walker
