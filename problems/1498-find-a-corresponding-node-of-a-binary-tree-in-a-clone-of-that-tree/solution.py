# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        stack = [(original, cloned)]
        while stack:
            original_node, cloned_node = stack.pop()
            if original_node == target: return cloned_node
            
            if original_node.left: stack.append((original_node.left, cloned_node.left))
            if original_node.right: stack.append((original_node.right, cloned_node.right))
