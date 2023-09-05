"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copy = defaultdict(lambda: Node(0), {None: None})
        
        node = head
        while node:
            copy_node = copy[node]
            copy_node.val = node.val
            copy_node.next = copy[node.next]
            copy_node.random = copy[node.random]
            node = node.next
        
        return copy[head]
            
