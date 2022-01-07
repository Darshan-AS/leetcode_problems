# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root_: Optional[TreeNode]) -> int:
        def max_path_sum(root: Optional[TreeNode]) -> tuple[int, int]:
            if not root: return (-math.inf, -math.inf)
            
            l_any_max, l_linear_max = max_path_sum(root.left)
            r_any_max, r_linear_max = max_path_sum(root.right)
            
            return (
                max(l_any_max, r_any_max, max(l_linear_max, 0) + root.val + max(r_linear_max, 0)),
                max(l_linear_max, r_linear_max, 0) + root.val
            )
        
        return max_path_sum(root_)[0]
