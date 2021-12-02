# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root_: Optional[TreeNode]) -> List[int]:
        def right_view(root):
            level = (root,) if root else tuple()
            while level:
                yield level[-1]
                level = tuple(child for node in level for child in (node.left, node.right) if child)
        
        return [node.val for node in right_view(root_)]
