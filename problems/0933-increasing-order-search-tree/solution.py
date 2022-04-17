# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def increasingBST(self, bst: TreeNode) -> TreeNode:
        def to_inorder_LL(root: TreeNode | None) -> tuple[TreeNode | None, TreeNode | None]:
            if root is None: return None, None
            
            l_head, l_tail = to_inorder_LL(root.left)
            r_head, r_tail = to_inorder_LL(root.right)
            
            if l_tail: l_tail.right = root
            root.left, root.right = None, r_head
            
            return l_head or root, r_tail or root
        
        return to_inorder_LL(bst)[0]
        
