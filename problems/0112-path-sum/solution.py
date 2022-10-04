# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode | None, target_sum: int) -> bool:
        if root is None: return False
        if root.left is None and root.right is None: return root.val == target_sum
        return (
            self.hasPathSum(root.left , target_sum - root.val) or
            self.hasPathSum(root.right, target_sum - root.val)
        )
