# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root_: Optional[TreeNode]) -> List[str]:
        def paths(root: Optional[TreeNode], path: list = None):
            path = [] if path is None else path
            if not root: return
            
            path.append(root.val)
            if not root.left and not root.right: yield iter(path)
            yield from paths(root.left, path)
            yield from paths(root.right, path)
            path.pop()
        
        return ['->'.join(map(str, path)) for path in paths(root_)]
            
