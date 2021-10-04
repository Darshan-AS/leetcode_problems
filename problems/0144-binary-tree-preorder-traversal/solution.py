# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def preorder(node: Optional[TreeNode]):
            if not node: return
            yield node.val
            yield from preorder(node.left)
            yield from preorder(node.right)
        
        return list(preorder(root))
