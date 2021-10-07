# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate_bst(
            bst: Optional[TreeNode], low: int = -math.inf, high: int = math.inf
        ) -> bool:
            return (
                low < bst.val < high
                and validate_bst(bst.left, low, bst.val)
                and validate_bst(bst.right, bst.val, high)
                if bst
                else True
            )
        
        return validate_bst(root)
