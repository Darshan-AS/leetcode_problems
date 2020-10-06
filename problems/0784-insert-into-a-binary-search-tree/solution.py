# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        node = root
        new_node = TreeNode(val)
        while node:
            if val < node.val:
                if not node.left:
                    node.left = new_node
                    return root
                node = node.left
            else:
                if not node.right:
                    node.right = new_node
                    return root
                node = node.right
        
        return new_node
