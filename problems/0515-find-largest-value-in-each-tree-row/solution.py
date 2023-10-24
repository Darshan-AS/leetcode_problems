# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: TreeNode | None) -> list[int]:
        def level_order(root: TreeNode | None) -> Iterator[tuple[TreeNode]]:
            level = () if root is None else (root,)
            while level:
                yield level
                level = tuple(child for node in level for child in (node.left, node.right) if child)
        
        return [max(node.val for node in l) for l in level_order(root)]
        
