# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def inorder(root):
            if not root:
                return
            yield from inorder(root.left)
            yield root.val
            yield from inorder(root.right)
        
        def merge(sort1, sort2):
            i = j = 0
            while i < len(sort1) and j < len(sort2):
                if (a := sort1[i]) < (b := sort2[j]):
                    yield a
                    i += 1
                else:
                    yield b
                    j += 1
            for x in range(i, len(sort1)): yield sort1[x]
            for y in range(j, len(sort2)): yield sort2[y]
        
        return list(merge(list(inorder(root1)), list(inorder(root2))))
