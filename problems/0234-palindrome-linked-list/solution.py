# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def isPalindrome(self, head_: Optional[ListNode]) -> bool:
        def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
            prev_node, curr_node = None, head

            while curr_node:
                next_node = curr_node.next
                curr_node.next = prev_node
                prev_node, curr_node = curr_node, next_node

            return prev_node
        
        def iter_list(head: Optional[ListNode]) -> iter:
            while head:
                yield head.val
                head = head.next
        
        walker = runner = head_
        while runner and runner.next:
            walker, runner = walker.next, runner.next.next
        
        fs, bs = head_, reverse_list(walker.next if runner else walker)
        return all(f == b for f, b in zip(iter_list(fs), iter_list(bs)))
