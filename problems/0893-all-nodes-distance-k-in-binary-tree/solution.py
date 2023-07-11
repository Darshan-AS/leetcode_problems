# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> list[int]:
        def find_rpath(src: TreeNode | None, dst: TreeNode | None) -> Iterator[TreeNode]:
            path = find_rpath(src.left, dst) or find_rpath(src.right, dst) if src else []
            return path.append(src) or path if path or (src == dst != None) else path
        
        def level_order(root: TreeNode, parents: Mapping[TreeNode, TreeNode] = None) -> Iterator[tuple[TreeNode]]:
            level, seen, parents = (root,), {root, None}, parents or {}
            while level:
                yield level
                level = tuple(child for node in level for child in (node.left, node.right, parents.get(node)) if child not in seen)
                seen.update(level)

        path = find_rpath(root, target)
        parents_map = dict(pairwise(path))
        kth_level = next(islice(level_order(target, parents_map), k, None), [])
        return [node.val for node in kth_level]

