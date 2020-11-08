# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: TreeNode) -> int:
        def post_order_sum(node):
            if not node: return 0, 0
            left_val_sum, left_tilt_sum = post_order_sum(node.left)
            right_val_sum, right_tilt_sum = post_order_sum(node.right)
            return (
                left_val_sum + right_val_sum + node.val,
                left_tilt_sum + right_tilt_sum + abs(right_val_sum - left_val_sum)
            )
        
        return post_order_sum(root)[1]
