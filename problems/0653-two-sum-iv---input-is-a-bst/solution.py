# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root_: TreeNode | None, k: int) -> bool:
        def inorder(root: TreeNode | None, reverse: bool=False) -> iter:
            if root is None: return
            first, last = (root.right, root.left) if reverse else (root.left, root.right)
            yield from inorder(first, reverse)
            yield root.val
            yield from inorder(last, reverse)
        
        left_gen, right_gen = inorder(root_), inorder(root_, reverse=True)
        left, right = next(left_gen), next(right_gen)
        while left < right:
            sum_ = left + right
            if sum_ < k: left = next(left_gen)
            elif sum_ > k: right = next(right_gen)
            else: return True
        return False

