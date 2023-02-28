# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root_: TreeNode | None) -> list[TreeNode | None]:
        counter = Counter()
        dups = []

        def serialize(root: TreeNode | None) -> str:
            if not root: return '#'
            s = ','.join((str(root.val), serialize(root.left), serialize(root.right)))
            counter[s] += 1
            if counter[s] == 2: dups.append(root)
            return s
        
        serialize(root_)
        return dups

        
