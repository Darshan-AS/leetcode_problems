# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        if not root: return root
        if d == 1: return TreeNode(v, left=root)
    
        depth = 1
        level = (root,)
        while depth + 1 < d:
            level = (child for node in level for child in (node.left, node.right) if child)
            depth += 1
        
        for node in level:
            node.left = TreeNode(v, left=node.left)
            node.right = TreeNode(v, right=node.right)
        
        return root
