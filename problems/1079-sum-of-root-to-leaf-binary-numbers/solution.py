# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        def find_binary_nums(root_node):            
            stack = [(root_node, 0)]
            while stack:
                node, n = stack.pop()
                n = n * 2 + node.val
                
                if not node.left and not node.right: yield n
                if node.left: stack.append((node.left, n))
                if node.right: stack.append((node.right, n))
            
        return sum(find_binary_nums(root))
