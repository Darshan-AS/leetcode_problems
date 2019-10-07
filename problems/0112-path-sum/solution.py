# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        
        stack = [(root, root.val)]
        while stack:
            node, current_sum = stack.pop()
            if current_sum == sum and not node.left and not node.right:
                return True
            
            if node.left:
                stack.append((node.left, current_sum + node.left.val))
                
            if node.right:
                stack.append((node.right, current_sum + node.right.val))
            
        return False
