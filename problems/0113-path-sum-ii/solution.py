# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root_: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def path_sum(root: Optional[TreeNode], target: int, path: list = None):
            path = [] if path is None else path
            if not root: return
            
            path.append(root.val)   
            if not root.left and not root.right and root.val == target: yield iter(path)
            yield from path_sum(root.left , target - root.val, path)
            yield from path_sum(root.right, target - root.val, path)
            path.pop()
        
        return list(map(list, path_sum(root_, targetSum, [])))

