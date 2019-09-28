# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        def is_mirror(a, b):
            if not a and not b:
                return True
            if not a or not b:
                return False
            if a.val != b.val:
                return False
            
            return is_mirror(a.right, b.left) and is_mirror(a.left, b.right)
        
        return is_mirror(root.right, root.left)
