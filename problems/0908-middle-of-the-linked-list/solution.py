# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        walker = runner = head
        
        while runner and runner.next:
            walker = walker.next
            runner = runner.next.next
        
        return walker
