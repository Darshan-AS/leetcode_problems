# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        def inorder(node: Optional[TreeNode]):
            if not node: return
            yield from inorder(node.left)
            yield node.val
            yield from inorder(node.right)
        
        def rev_inorder(node: Optional[TreeNode]):
            if not node: return
            yield from rev_inorder(node.right)
            yield node.val
            yield from rev_inorder(node.left)
        
        incr, decr = inorder(root), rev_inorder(root)
        left, right = next(incr), next(decr)
        while left < right:
            sum_ = left + right
            if sum_ > k:
                right = next(decr)
            elif sum_ < k:
                left = next(incr)
            else:
                return True
        
        return False
