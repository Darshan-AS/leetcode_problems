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
        level = (root,) if root else ()
        while level:
            for i in range(len(level) - 1): level[i].next = level[i + 1]
            level = tuple(child for node in level for child in (node.left, node.right) if child)
        return root
