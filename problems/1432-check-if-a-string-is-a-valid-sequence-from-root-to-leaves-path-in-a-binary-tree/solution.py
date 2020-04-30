# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        n = len(arr)
        
        def dfs(node, index):
            l_value = dfs(node.left, index + 1) if node.left else False
            r_value = dfs(node.right, index + 1) if node.right else False
            child_val = True if not node.left and not node.right and index == n - 1 else (l_value or r_value)
            
            return index < n and node.val == arr[index] and child_val
        
        return dfs(root, 0)
