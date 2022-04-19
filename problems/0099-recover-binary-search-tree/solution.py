# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def recoverTree(self, bst: TreeNode | None) -> None:
        
        def inorder(root: TreeNode | None) -> Iterator[TreeNode]:
            if not root: return
            
            yield from inorder(root.left)
            yield root
            yield from inorder(root.right)
        
        wrong_pairs = tuple((x, y) for x, y in pairwise(inorder(bst)) if x.val > y.val)
        (node_a, _), (_, node_b) = wrong_pairs[0], wrong_pairs[-1]
        node_a.val, node_b.val = node_b.val, node_a.val
        
