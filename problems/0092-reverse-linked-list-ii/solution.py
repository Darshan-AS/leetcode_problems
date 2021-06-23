# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        new_head = ListNode(-1, next=head)
        
        left_end = new_head
        for _ in range(left - 1):
            left_end = left_end.next
        
        prev_node, curr_node = None, left_end.next
        for _ in range(left, right + 1):
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node, curr_node = curr_node, next_node
        
        left_end.next.next = curr_node
        left_end.next = prev_node
        
        return new_head.next
        
