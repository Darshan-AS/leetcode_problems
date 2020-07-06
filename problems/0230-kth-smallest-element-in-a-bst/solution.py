# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        
        node = None
        while k:
            while root:
                stack.append(root)
                root = root.left
            node = stack.pop()
            k -= 1
            root = node.right
        return node.val
