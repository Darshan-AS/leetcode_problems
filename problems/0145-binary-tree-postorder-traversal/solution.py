# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root_: Optional[TreeNode]) -> List[int]:
        def postorder(root: Optional[TreeNode]):
            stack = [root] if root else []
            
            while stack:
                node = stack.pop()
                if not node.left and not node.right: yield node.val; continue
                
                stack.append(TreeNode(node.val))
                if node.right: stack.append(node.right)
                if node.left: stack.append(node.left)
                
        return list(postorder(root_))
