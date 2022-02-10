# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def generateTrees(self, n: int) -> list[TreeNode | None]:
        def gen_trees(start: int, end: int) -> Iterator[TreeNode | None]:
            return (
                TreeNode(value, deepcopy(left), deepcopy(right))
                for value in range(start, end)
                for left in gen_trees(start, value)
                for right in gen_trees(value + 1, end)
            ) if start < end else (None,)
        
        return list(gen_trees(1, n + 1))
