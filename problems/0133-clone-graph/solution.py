"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:    
    def cloneGraph(self, input_node: 'Node') -> 'Node':
        if not input_node: return input_node
        
        def deep_copy(node):
            if node not in seen_old_to_new:
                seen_old_to_new[node] = new_node = Node(node.val)
                new_node.neighbors = list(map(deep_copy, node.neighbors))
            return seen_old_to_new[node]
        
        seen_old_to_new = {}
        return deep_copy(input_node)
