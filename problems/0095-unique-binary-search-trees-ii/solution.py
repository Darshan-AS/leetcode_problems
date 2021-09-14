# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from itertools import product

class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def gen_trees(left: int, right: int) -> List[Optional[TreeNode]]:
            if left == right:
                yield None
                return
            
            for i in range(left, right):
                for l, r in product(list(gen_trees(left, i)), list(gen_trees(i + 1, right))):
                    yield TreeNode(i, l, r)
        
        return list(gen_trees(1, n + 1))
