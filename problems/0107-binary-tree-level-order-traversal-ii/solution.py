# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        result = []
        if not root:
            return result
        
        queue = deque([(root, 1)])
        curr_level = 1
        curr_result = []
        while queue:
            node, level = queue.popleft()
            if not node:
                continue
                
            if level == curr_level:
                curr_result.append(node.val)
            else:
                curr_level = level
                result.append(curr_result)
                curr_result = [node.val]
            
            queue.append((node.left, level + 1))
            queue.append((node.right, level + 1))
            
        result.append(curr_result)
        return reversed(result)
