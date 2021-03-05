# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        level = (root,)
        while level:
            yield sum(node.val for node in level) / len(level)
            level = tuple(child for node in level for child in (node.left, node.right) if child)
