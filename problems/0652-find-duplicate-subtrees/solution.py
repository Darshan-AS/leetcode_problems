# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root_: TreeNode | None) -> list[TreeNode | None]:
        ids_pool = count(1)
        ids_count = Counter()
        ids_seen = {}
        dups = []

        Id = int | None
        def helper(root: TreeNode | None) -> Id:
            if not root: return
            triple = (str(root.val), helper(root.left), helper(root.right))
            id_ = ids_seen.get(triple, next(ids_pool))
            ids_seen[triple] = id_
            ids_count[id_] += 1
            if ids_count[id_] == 2: dups.append(root)
            return id_
        
        helper(root_)
        return dups

        
