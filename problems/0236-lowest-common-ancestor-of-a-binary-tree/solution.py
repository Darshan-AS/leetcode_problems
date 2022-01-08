# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root_: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def lca_for_p_q(root: Optional[TreeNode]) -> tuple[Optional[TreeNode], bool]:
            if not root: return root, False
            
            l_lca, l_has_p_or_q = lca_for_p_q(root.left)
            r_lca, r_has_p_or_q = lca_for_p_q(root.right)
            root_is_p_or_q = root in (p, q)
            
            return (
                root if (l_has_p_or_q + r_has_p_or_q + root_is_p_or_q) >= 2 else (l_lca or r_lca),
                l_has_p_or_q or r_has_p_or_q or root_is_p_or_q
            )
        
        return lca_for_p_q(root_)[0]
