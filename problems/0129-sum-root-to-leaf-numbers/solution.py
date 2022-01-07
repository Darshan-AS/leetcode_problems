# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root_: Optional[TreeNode]) -> int:
        def path_numbers(root: Optional[TreeNode], n: int = 0):
            if not root: return
            
            next_n = n * 10 + root.val
            if not root.left and not root.right: yield next_n
            yield from path_numbers(root.left , next_n)
            yield from path_numbers(root.right, next_n)
        
        return sum(path_numbers(root_))
