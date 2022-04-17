# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def increasingBST(self, bst: TreeNode) -> TreeNode:
        def inorder_nodes(root: TreeNode | None) -> Iterable[TreeNode]:
            if not root: return
            
            l_node, r_node = root.left, root.right
            root.left = root.right = None
            
            yield from inorder_nodes(l_node)
            yield root
            yield from inorder_nodes(r_node)
        
        def peek(iterable: Iterable[Any]) -> tuple[Any, Iterable[Any]]:
            head = next(iterable, None)
            return head, chain((head,), iterable)
        
        def thread_nodes(nodes: Iterable[TreeNode]) -> TreeNode | None:
            head, nodes = peek(nodes)
            for a, b in pairwise(nodes): a.right = b
            return head
        
        return thread_nodes(inorder_nodes(bst))
        
        
