# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def convertBST(self, bst: TreeNode | None) -> TreeNode | None:
        
        def to_greater_tree(root: TreeNode | None, acc: int = 0) -> tuple[TreeNode | None, int]:
            if not root: return None, 0
            
            r_node, r_sum = to_greater_tree(root.right, acc)
            root_val = root.val + r_sum + acc
            l_node, l_sum = to_greater_tree(root.left, root_val)

            return TreeNode(root_val, l_node, r_node), l_sum + root.val + r_sum
        
        return to_greater_tree(bst)[0]
