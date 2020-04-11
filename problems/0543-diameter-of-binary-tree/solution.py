# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.diameter = 0
        
        def depth(node):
            if not node:
                return 0
            l_depth = depth(node.left)
            r_depth = depth(node.right)
            self.diameter = max(self.diameter, l_depth + r_depth)
            return max(l_depth, r_depth) + 1
        
        depth(root)
        return self.diameter
