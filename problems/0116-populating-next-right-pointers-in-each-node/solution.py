"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not (root and root.left and root.right): return root
        
        left_node, right_node = self.connect(root.left), self.connect(root.right)
        while left_node and right_node:
            left_node.next = right_node
            left_node, right_node = left_node.right, right_node.left
            
        return root
