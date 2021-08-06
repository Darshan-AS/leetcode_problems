"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        level = (root,) if root else tuple()
        while level:
            yield map(lambda n: n.val, level)
            level = tuple(child for node in level for child in node.children)

