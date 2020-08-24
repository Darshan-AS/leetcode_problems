# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:    
        stack = [(root, False)] if root else []
        
        left_sum = 0
        while stack:
            node, is_left = stack.pop()
            if is_left and not node.left and not node.right:
                left_sum += node.val
            
            if node.left: stack.append((node.left, True))
            if node.right: stack.append((node.right, False))
        return left_sum
