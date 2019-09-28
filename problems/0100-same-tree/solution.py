# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
#         # Recursive
#         if not p and not q:
#             return True
#         elif not p or not q:
#             return False
#         
#         return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        
        # Iterative
        stack = [(p, q)]
        while stack:
            p, q = stack.pop()
            
            if not p and not q:
                continue
            elif not p or not q:
                return False
            
            if p.val != q.val:
                return False
            
            stack.append((p.left, q.left))
            stack.append((p.right, q.right))
        
        return True
