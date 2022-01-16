# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root_: Optional[TreeNode]) -> int:
        def left_most_height(root: Optional[TreeNode]) -> int:
            h = 0
            node = root
            while node:
                node = node.left
                h += 1
            return h
        
        # return n**0 + n**1 + n**2 + ... + n**k
        def powers_sum(n: int, k: int) -> int:
            return n ** k - 1
        
        def count_nodes(root: Optional[TreeNode], l_height: int = None, r_height: int = None) -> int:
            if not root: return 0
            
            l_height = left_most_height(root.left) if l_height is None else l_height
            r_height = left_most_height(root.right) if r_height is None else r_height
            
            return (
                powers_sum(2, l_height) + 1 + count_nodes(root.right, r_height - 1)
                if l_height == r_height
                else count_nodes(root.left, l_height - 1) + 1 + powers_sum(2, r_height)
            )
        
        return count_nodes(root_)
