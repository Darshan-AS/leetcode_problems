# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: TreeNode | None) -> list[int]:
        def inorder(root: TreeNode | None) -> Iterator[TreeNode]:
            yield from chain(inorder(root.left), (root,), inorder(root.right)) if root else ()

        def collect_modes(mode_freqs, x_freqs):
            (modes, max_freq), (x, freq) = mode_freqs, x_freqs
            if freq < max_freq: return mode_freqs
            elif freq > max_freq: return ([x], freq)
            else: return (modes.append(x) or modes, freq)
        
        xs = map(lambda x: x.val, inorder(root))
        x_counts = ((x, sum(1 for _ in g)) for x, g in groupby(xs))
        return reduce(collect_modes, x_counts, ([], 0))[0]
