# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        root = TreeNode(preorder[0])
        stack = [root]
        
        for i in range(1, len(preorder)):
            node, child = stack[-1], TreeNode(preorder[i])
            
            while stack and stack[-1].val < child.val:
                node = stack.pop()
                
            if child.val < node.val:
                node.left = child
            elif child.val > node.val:
                node.right = child
            
            stack.append(child)
        
        return root
