# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        walker = runner = head
        
        while runner and runner.next:
            walker = walker.next
            runner = runner.next.next
            if walker == runner: break
        else: return
        
        walker_a, walker_b = head, walker
        while walker_a != walker_b:
            walker_a = walker_a.next
            walker_b = walker_b.next
        
        return walker_a
