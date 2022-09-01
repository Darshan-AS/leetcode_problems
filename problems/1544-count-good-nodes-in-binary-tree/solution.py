# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root_: TreeNode) -> int:
        def count_good_nodes(root: TreeNode | None, max_parent: int=-math.inf) -> int:
            return (
                int(max_parent <= root.val) +
                count_good_nodes(root.left, max(max_parent, root.val)) +
                count_good_nodes(root.right, max(max_parent, root.val))
            ) if root else 0
        
        return count_good_nodes(root_)
