# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root_: Optional[TreeNode]) -> List[int]:
        # Morris (Destroys the tree)
        def inorder(root: Optional[TreeNode]):
            node = root
            while node:
                if node.left:
                    last = node.left
                    while last.right: last = last.right
                    
                    last.right = node
                    node = node.left
                    last.right.left = None
                else:
                    yield node.val
                    node = node.right
                
        return list(inorder(root_))
