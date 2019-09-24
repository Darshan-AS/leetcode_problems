# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        
        curr = runner = head
        while runner:
            if runner.val != curr.val:
                curr.next = runner
                curr = runner
            
            runner = runner.next
        curr.next = None
        
        return head
