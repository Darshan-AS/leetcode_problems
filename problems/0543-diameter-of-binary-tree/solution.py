# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def diam_and_depth(node):
            if not node: return 0, 0
            l_diam, l_depth = diam_and_depth(node.left)
            r_diam, r_depth = diam_and_depth(node.right)
            return max(l_diam, r_diam, l_depth + r_depth), max(l_depth, r_depth) + 1
        
        return diam_and_depth(root)[0]
