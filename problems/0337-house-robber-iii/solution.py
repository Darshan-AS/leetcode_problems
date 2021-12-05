# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root_: Optional[TreeNode]) -> int:
        def rob_tree(root) -> tuple[int, int]:
            if not root: return 0, 0
            bests_and_prev_bests = (rob_tree(node) for node in (root.left, root.right))
            bests, prev_bests = zip(*bests_and_prev_bests)
            return max(sum(prev_bests) + root.val, sum(bests)), sum(bests)
        
        return rob_tree(root_)[0]
