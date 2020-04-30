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
            if not node or index == n:
                return False

            if not node.left and not node.right and index == n - 1 and node.val == arr[index]:
                return True
            
            return node.val == arr[index] and (dfs(node.left, index+1) or dfs(node.right, index+1))
        
        return dfs(root, 0)
