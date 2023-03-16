# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int]) -> TreeNode | None:
        in_index_map = dict(map(reversed, enumerate(inorder)))
        
        def build_tree(post_end: int, in_start: int, in_end: int) -> tuple[TreeNode | None, int]:
            if in_start >= in_end: return None, post_end
            
            root_val = postorder[post_end]
            root_index = in_index_map[root_val]
            
            r_tree, post_start = build_tree(post_end - 1, root_index + 1, in_end)
            l_tree, post_start = build_tree(post_start, in_start, root_index)
            
            return TreeNode(root_val, l_tree, r_tree), post_start
        
        return build_tree(len(postorder) - 1, 0, len(inorder))[0]
        
