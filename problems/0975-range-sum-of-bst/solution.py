# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sum_all(self, root: TreeNode):
        if not root: return 0
        return self.sum_all(root.left) + root.val + self.sum_all(root.right)
    
    def sum_greater(self, root: TreeNode, n: int):
        if not root: return 0
        
        if root.val < n:
            return self.sum_greater(root.right, n)
        else:
            return self.sum_greater(root.left, n) + root.val + self.sum_all(root.right)
    
    def sum_lesser(self, root: TreeNode, n: int):
        if not root: return 0
        
        if root.val > n:
            return self.sum_lesser(root.left, n)
        else:
            return self.sum_all(root.left) + root.val + self.sum_lesser(root.right, n) 
    
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        if not root: return 0
        
        if low <= high < root.val:
            return self.rangeSumBST(root.left, low, high)
        elif root.val < low <= high:
            return self.rangeSumBST(root.right, low, high)
        else:
            return self.sum_greater(root.left, low) + root.val + self.sum_lesser(root.right, high)
