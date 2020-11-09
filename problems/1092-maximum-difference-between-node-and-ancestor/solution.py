# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        max_diff = 0
        stack = [(root, root.val, root.val)]
        while stack:
            node, curr_max, curr_min = stack.pop()
            max_diff = max(max_diff, abs(curr_max - node.val), abs(curr_min - node.val))
            next_max, next_min = max(curr_max, node.val), min(curr_min, node.val)
            if node.left: stack.append((node.left, next_max, next_min))
            if node.right: stack.append((node.right, next_max, next_min))
        return max_diff
