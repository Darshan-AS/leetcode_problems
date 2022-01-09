# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root_: TreeNode, target_: TreeNode, k_: int) -> List[int]:
        def pairwise(iterable):
            a, b = tee(iterable)
            next(b, None)
            return zip(a, b)
        
        def find_path(root: Optional[TreeNode], target: TreeNode) -> Iterator[TreeNode]:
            if not root: return deque()
            if root == target: return deque([root])
            
            path = find_path(root.left, target) or find_path(root.right, target)
            if path: path.appendleft(root)
            
            return path
        
        def k_dist_away(
            root: Optional[TreeNode],
            k: int,
            parent_map: dict[TreeNode, TreeNode] = None,
        ) -> Iterator[Iterator[TreeNode]]:
            parent_map = parent_map if parent_map else {}
            
            queue = deque([(root, 0)]) if root else deque()
            seen = {root}
            
            while queue:
                node, dist = queue.popleft()
                if dist == k:
                    yield node
                    continue
                
                for child in (node.left, node.right, parent_map.get(node)):
                    if child  and child not in seen:
                        queue.append((child, dist + 1))
                        seen.add(child)
        
        path = find_path(root_, target_)
        parent_map = dict(pairwise(reversed(path)))
        return [node.val for node in k_dist_away(target_, k_, parent_map)]
        
        
