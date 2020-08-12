# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class LL_Node:
    def __init__(self, *items):
        self.__items = list(items) if items else []
        self.next = None
        
    def __iter__(self):
        return map(lambda x: x[1], sorted(self.__items))
        
    def add(self, y, item):
        self.__items.append((y, item))

class Solution:
    # x denotes vertical_index and y denotes depth of a node
    # Assuming the (x, y) = (0, 0) starts at top-left corner
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        hash_map = {0: LL_Node()}
        queue = deque([(0, 0, root)])
        start_x = 0
        
        while queue:
            x, y, node = queue.popleft()
            start_x = min(start_x, x)
            
            if x in hash_map:
                hash_map[x].add(y, node.val)
            else:
                hash_map[x] = LL_Node((y, node.val))
                if x > 0:
                    hash_map[x - 1].next = hash_map[x]
                else:
                    hash_map[x].next = hash_map[x + 1]
            
            if node.left: queue.append((x - 1, y + 1, node.left))
            if node.right: queue.append((x + 1, y + 1, node.right))
        
        ans = []
        curr = hash_map[start_x]
        while curr:
            ans.append(list(curr))
            curr = curr.next
        return ans

