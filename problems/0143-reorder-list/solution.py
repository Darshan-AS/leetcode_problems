# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        node_pointers = []
        curr = head
        while curr:
            node_pointers.append(curr)
            curr = curr.next
        
        i, j = 0, len(node_pointers) - 1
        prev_node = ListNode()
        while i < j:
            left_node, right_node = node_pointers[i], node_pointers[j]
            prev_node.next = left_node
            left_node.next = right_node
            prev_node = right_node
            i += 1
            j -= 1
        
        if i == j:
            prev_node.next = node_pointers[i]
            prev_node = prev_node.next
        prev_node.next = None
        
