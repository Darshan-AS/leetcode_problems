# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def preorderTraversal(self, root_: TreeNode | None) -> list[int]:
        # Morris (Destroys and recovers the tree)
        def preorder(root: TreeNode | None) -> Iterable:
            node = root
            while node:
                if node.left is None:
                    yield node.val
                    node = node.right
                    continue

                last = node.left
                while last.right and last.right != node:
                    last = last.right
                
                if last.right is None:
                    yield node.val
                    last.right = node
                    node = node.left
                else:
                    last.right = None
                    node = node.right
                
        return list(preorder(root_))
