# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: TreeNode | None, key_: int) -> TreeNode | None:
        def pop_min(bst: TreeNode | None) -> tuple[TreeNode | None, TreeNode | None]:
            parent, child = None, bst
            while child and child.left:
                parent, child = child, child.left
            
            if not parent: return child, child.right
            
            parent.left = child.right
            return child, bst
        
        def delete(bst: TreeNode | None, key: Any) -> TreeNode | None:
            if not bst: return bst

            if key < bst.val:
                bst.left = delete(bst.left, key)
            elif key > bst.val:
                bst.right = delete(bst.right, key)
            else:
                if not bst.left:
                    bst = bst.right
                elif not bst.right:
                    bst = bst.left
                else:
                    min_node, right_bst = pop_min(bst.right)
                    bst.right = right_bst
                    
                    min_node.left, min_node.right = bst.left, bst.right
                    bst.left, bst.right = None, None
                    
                    bst = min_node
            return bst
        
        return delete(root, key_)
                
