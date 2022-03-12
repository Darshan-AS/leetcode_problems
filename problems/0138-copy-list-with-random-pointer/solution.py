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
        to_copy = defaultdict(lambda: Node(0), {None: None})
        
        node = head
        while node:
            copy_node = to_copy[node]
            copy_node.val = node.val
            copy_node.next = to_copy[node.next]
            copy_node.random = to_copy[node.random]
            node = node.next
        
        return to_copy[head]
            
