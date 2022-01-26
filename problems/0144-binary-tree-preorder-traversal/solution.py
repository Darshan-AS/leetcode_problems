# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root_: Optional[TreeNode]) -> List[int]:
        # Morris (Destroys and recovers the tree)
        def preorder(root: Optional[TreeNode]):
            node = root
            while node:
                yield node.val
                if node.left:
                    last = node.left
                    while last.right and last.right != node.right:
                        last = last.right
                    
                    if last.right:
                        last.right = None
                        node = node.right
                    else:
                        last.right = node.right
                        node = node.left
                else:
                    node = node.right
                
        return list(preorder(root_))
