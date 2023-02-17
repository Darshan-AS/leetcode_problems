# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root_: TreeNode | None) -> int:
        def inorder(root: TreeNode | None) -> Iterable[int]:
            yield from chain(inorder(root.left), (root,), inorder(root.right)) if root else tuple()
        
        return min(b.val - a.val for a, b in pairwise(inorder(root_)))
