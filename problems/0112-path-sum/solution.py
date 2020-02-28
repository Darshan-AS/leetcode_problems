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
        
        stack = [(root, 0)]
        while stack:
            node, s = stack.pop()
            s += node.val
            
            if not node.left and not node.right and s == sum:
                return True
            
            if node.left: stack.append((node.left, s))
            if node.right: stack.append((node.right, s))
        
        return False
