# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root_: Optional[TreeNode]) -> List[int]:
        # Morris (Destroys and recovers the tree)
        def inorder(root: Optional[TreeNode]):
            node = root
            while node:
                if node.left:
                    last = node.left
                    while last.right and last.right != node:
                        last = last.right
                    
                    if last.right:
                        last.right = None
                        yield node.val
                        node = node.right
                    else:
                        last.right = node
                        node = node.left
                else:
                    yield node.val
                    node = node.right
        
        return list(inorder(root_))
