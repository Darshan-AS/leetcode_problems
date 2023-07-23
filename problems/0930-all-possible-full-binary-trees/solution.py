# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> list[TreeNode | None]:
        return [
            TreeNode(0, lt, rt)
            for i in range(1, n - 1, 2)
            for lt in self.allPossibleFBT(i)
            for rt in self.allPossibleFBT(n - i - 1)
        ] if n > 1 else [TreeNode()]
