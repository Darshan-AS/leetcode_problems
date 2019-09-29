# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        # return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1 # Recursive
        
        max_depth = depth = 1
        stack = [(root.left, root.right, depth)]
        while stack:
            a, b, d = stack.pop()
            
            if not a and not b:
                max_depth = max(max_depth, d)
                
            if a:
                stack.append((a.left, a.right, d + 1))
            if b:
                stack.append((b.left, b.right, d + 1))
        
        return max_depth
