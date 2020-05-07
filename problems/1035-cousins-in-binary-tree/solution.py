# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        queue = [(root, 0)]
        x_info = y_info = None
        
        while queue:
            node, depth = queue.pop()
            left_val = right_val = -1
            if node.left:
                left_val = node.left.val
                queue.append((node.left, depth + 1))
            if node.right:
                right_val = node.right.val
                queue.append((node.right, depth + 1))
            
            if x in [left_val, right_val]:
                x_info = (node, depth)
            if y in [left_val, right_val]:
                y_info = (node, depth) 
            
            if x_info and y_info and x_info[1] == y_info[1] and x_info[0] != y_info[0]:
                return True
        
        return False
            
            
            
