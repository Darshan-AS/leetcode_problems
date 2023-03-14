# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root_: TreeNode | None) -> int:
        def path_numbers(root: TreeNode | None, n: int = 0) -> Iterator[int]:
            if root is None: return

            n_ = n * 10 + root.val
            if root.left == None == root.right: yield n_; return
            
            yield from path_numbers(root.left , n_)
            yield from path_numbers(root.right, n_)
        
        return sum(path_numbers(root_))
