# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False
        
        walker, runner = head, head.next
        
        while walker != runner:
            if not runner or not runner.next:
                return False
            
            walker = walker.next
            runner = runner.next.next
        
        return True
