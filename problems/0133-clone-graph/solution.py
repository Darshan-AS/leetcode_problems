"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def __init__(self):
        self.seen_old_to_new = {}
        
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return node
        
        if node not in self.seen_old_to_new:
            self.seen_old_to_new[node] = new_node = Node(node.val)
            new_node.neighbors = list(map(self.cloneGraph, node.neighbors))
        return self.seen_old_to_new[node]
