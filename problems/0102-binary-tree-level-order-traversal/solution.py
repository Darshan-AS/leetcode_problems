# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root_: Optional[TreeNode]) -> List[List[int]]:
        def level_order(root: Optional[TreeNode]):            
            level = (root,) if root else ()
            while level:
                yield (node.val for node in level)
                level = tuple(child for node in level for child in (node.left, node.right) if child)
            
        return list(map(list, level_order(root_)))
