# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def inorder(node: Optional[TreeNode]):
            if not node: return
            yield from inorder(node.left)
            yield node.val
            yield from inorder(node.right)
        
        return list(inorder(root))
