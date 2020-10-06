# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        new_node = TreeNode(val)
        if not root: return new_node
        
        curr, prev = root, None
        while curr:
            prev = curr
            curr = curr.left if val < curr.val else curr.right
        
        if val < prev.val: prev.left = new_node
        else: prev.right = new_node
        return root
