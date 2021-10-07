# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root_node: Optional[TreeNode], k: int) -> bool:
        def inorder(root: Optional[TreeNode], reverse: bool=False) -> iter:
            if not root: return
            yield from inorder(root.left) if not reverse else inorder(root.right, reverse=True)
            yield root.val
            yield from inorder(root.right) if not reverse else inorder(root.left, reverse=True)
            
        left_gen, right_gen = inorder(root_node), inorder(root_node, reverse=True)
        left, right = next(left_gen), next(right_gen)
        while left < right:
            sum_ = left + right
            if sum_ < k:
                left = next(left_gen)
            elif sum_ > k:
                right = next(right_gen)
            else:
                return True
        return False
