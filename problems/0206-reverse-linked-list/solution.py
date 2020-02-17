# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev_node, curr_node = None, head
        
        while curr_node:
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node, curr_node = curr_node, next_node
        
        return prev_node
