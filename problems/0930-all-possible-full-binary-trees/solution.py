# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> list[TreeNode | None]:
        return reduce(
            lambda a, n: setitem(a, n, [
                TreeNode(0, lt, rt)
                for i in range(1, n - 1, 2)
                for lt in a[i]
                for rt in a[n - i - 1]
            ]) or a,
            range(2, n + 1), {1: [TreeNode()]},
        )[n]
        
