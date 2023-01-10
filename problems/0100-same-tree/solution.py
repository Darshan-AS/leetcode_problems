# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        match (p, q):
            case (None, None): return True
            case (None, _) | (_, None): return False
            case (p, q): return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
