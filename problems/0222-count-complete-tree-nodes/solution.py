# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root_: TreeNode | None) -> int:
        def height(c_root: TreeNode | None, left: bool=True) -> int:
            h = 0
            while c_root:
                h += 1
                c_root = c_root.left if left else c_root.right
            return h
        
        
        root = root_
        count = 0
        while root and (lh := height(root.left, left=True)) != (rh := height(root.right, left=False)):
            midh = height(root.left, left=False)
            
            root, h = (root.right, lh) if midh == lh else (root.left, rh)
            count += 2 ** h

        return count + (0 if root is None else 2 ** (lh + 1) - 1)
