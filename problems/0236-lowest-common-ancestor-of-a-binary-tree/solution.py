# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode | None, p: TreeNode | None, q: TreeNode | None) -> TreeNode | None:
        if root in (None, p, q): return root
        
        left  = self.lowestCommonAncestor(root.left , p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        return root if left and right else (left or right)
