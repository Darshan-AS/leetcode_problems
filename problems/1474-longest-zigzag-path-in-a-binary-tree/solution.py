# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: TreeNode | None) -> int:
        def longest_zig_zag(node: TreeNode | None) -> tuple[int, int, int]:
            if node is None: return -1, -1, -1

            _, lt_node_max, lt_tree_max = longest_zig_zag(node.left)
            rt_node_max, _, rt_tree_max = longest_zig_zag(node.right)

            lt, rt = lt_node_max + 1, rt_node_max + 1
            return lt, rt, max(lt_tree_max, rt_tree_max, lt, rt)
        
        return longest_zig_zag(root)[-1]
