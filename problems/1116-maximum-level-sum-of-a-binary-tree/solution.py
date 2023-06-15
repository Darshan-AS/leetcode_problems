# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: TreeNode | None) -> int:
        def level_order(tree: TreeNode | None):
            level = (tree,) if tree else ()
            while level:
                yield level
                level = tuple(child for node in level for child in (node.left, node.right) if child)
        
        level_sums = (sum(x.val for x in xs) for xs in level_order(root))
        return max(enumerate(level_sums, 1), key=itemgetter(1), default=(0, 0))[0]
