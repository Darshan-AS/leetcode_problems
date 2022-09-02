# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root_: TreeNode | None) -> list[float]:
        def level_order(root: TreeNode | None):
            level = (root,) if root else tuple()
            while level:
                yield tuple(node.val for node in level)
                level = tuple(child for node in level for child in (node.left, node.right) if child)
        
        average = lambda xs: sum(xs) / len(xs)
        return list(map(average, level_order(root_)))
