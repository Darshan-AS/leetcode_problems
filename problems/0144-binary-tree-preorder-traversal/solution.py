# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root_: Optional[TreeNode]) -> List[int]:
        def preorder(root: Optional[TreeNode]):
            stack = [root] if root else []
            
            while stack:
                node = stack.pop()
                if not node.left and not node.right: yield node.val; continue
                
                if node.right: stack.append(node.right)
                if node.left: stack.append(node.left)
                stack.append(TreeNode(node.val))
                
        return list(preorder(root_))
