# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
    
        queue = deque([(root, 1)])
        while queue:
            node, depth = queue.popleft()
            left, right  = node.left, node.right
            if not left and not right:
                return depth
            
            if left:
                queue.append((left, depth + 1))
            if right:
                queue.append((right, depth + 1))
        
        return depth
            
        
