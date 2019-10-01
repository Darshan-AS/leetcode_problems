# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def is_balanced_helper(self, root: TreeNode) -> (bool, int):
        if not root:
            return True, -1
        
        left_balanced, left_height = self.is_balanced_helper(root.left)
        right_balanced, right_height = self.is_balanced_helper(root.right)
        
        if left_balanced and right_balanced and abs(right_height - left_height) <= 1:
            return True, max(right_height, left_height) + 1
        else:
            return False, max(right_height, left_height) + 1
        
    def isBalanced(self, root: TreeNode) -> bool:
        return self.is_balanced_helper(root)[0]
        
