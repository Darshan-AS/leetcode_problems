# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.vals_gen = BSTIterator.inorder(self.root)

    def next(self) -> int:
        return next(self.vals_gen)

    def hasNext(self) -> bool:
        x = next(self.vals_gen, None)
        if x is not None:
            self.vals_gen = chain((x,), self.vals_gen)
        return x is not None
    
    @staticmethod
    def inorder(root):
        if not root: return
        yield from BSTIterator.inorder(root.left)
        yield root.val
        yield from BSTIterator.inorder(root.right)
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
