# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: TreeNode | None, val: int, depth: int) -> TreeNode | None:
        if root is None: return root
        if depth == 1: return TreeNode(val, left=root)
        
        root.left = (
            TreeNode(val, left=root.left)
            if depth == 2 else
            self.addOneRow(root.left , val, depth - 1)
        )
        
        root.right = (
            TreeNode(val, right=root.right)
            if depth == 2 else
            self.addOneRow(root.right, val, depth - 1)
        )
        
        return root
