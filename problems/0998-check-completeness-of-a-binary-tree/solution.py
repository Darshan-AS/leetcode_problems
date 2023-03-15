# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root_: TreeNode | None) -> bool:
        def preorder(root: TreeNode | None, complete: bool=False) -> Iterator[TreeNode | None]:
            queue = deque((root,))
            while queue:
                node = queue.popleft()
                if complete or node: yield node
                queue.extend((node.left, node.right) if node else tuple())

        return not any(dropwhile(lambda x: x is not None, preorder(root_, complete=True)))
