# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def is_mirror(self, a, b):
            if not a and not b:
                return True
            if not a or not b:
                return False
            if a.val != b.val:
                return False
            
            return self.is_mirror(a.right, b.left) and self.is_mirror(a.left, b.right)
        
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        # return self.is_mirror(root.right, root.left) # recursive
        
        # Iterative
        stack = [(root.right, root.left)]
        while stack:
            a, b = stack.pop()
            if not a and not b:
                continue
            elif not a or not b:
                return False
            
            if a.val != b.val:
                return False
            
            stack.append((a.right, b.left))
            stack.append((a.left, b.right))
        
        return True
    
