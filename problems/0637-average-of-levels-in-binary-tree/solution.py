# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        averages = []
        if not root: return averages
        
        queue = deque([(root, 0)])
        level = 0
        
        while queue:
            sum_ = count = 0
            
            while queue and queue[0][1] == level:
                node, level = queue.popleft()
                sum_ += node.val
                count += 1
                
                if node.left: queue.append((node.left, level + 1))
                if node.right: queue.append((node.right, level + 1))
            
            level += 1
            averages.append(sum_ / count)
            
        return averages
