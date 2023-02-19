# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root_: TreeNode | None) -> list[list[int]]:
        def zigzag_level_order(root: TreeNode | None) -> Iterator[TreeNode]:
            level = (root,) if root else ()
            reverse = False
            while level:
                yield reversed(level) if reverse else iter(level)
                level = tuple(child for node in level for child in (node.left, node.right) if child)
                reverse = not reverse
        
        return [[node.val for node in level] for level in zigzag_level_order(root_)]
                
