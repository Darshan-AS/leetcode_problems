# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.max_sum = float('-inf')
        
        def depth_first_sum(node):
            if not node:
                return 0
            
            l_max_sum = max(depth_first_sum(node.left), 0)
            r_max_sum = max(depth_first_sum(node.right), 0)
            self.max_sum = max(self.max_sum, l_max_sum + r_max_sum + node.val)
            return max(l_max_sum, r_max_sum, 0) + node.val
        
        depth_first_sum(root)
        return self.max_sum
            
