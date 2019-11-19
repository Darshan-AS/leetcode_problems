# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return
        
        nodes_to_swap = collections.deque([root])
        
        while nodes_to_swap:
            node = nodes_to_swap.popleft()
            node.left, node.right = node.right, node.left
            
            if node.left:
                nodes_to_swap.append(node.left)
            if node.right:
                nodes_to_swap.append(node.right)
        
        return root
