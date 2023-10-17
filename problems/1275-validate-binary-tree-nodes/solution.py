class Solution:
    def validateBinaryTreeNodes(self, n: int, l_child: list[int], r_child: list[int]) -> bool:
        def is_valid_bt(root, seen) -> bool:
            return root == -1 or (root not in seen and (seen.add(root) or (
                is_valid_bt(l_child[root], seen) and is_valid_bt(r_child[root], seen))))

        roots = set(range(n)) - set(chain(l_child, r_child))
        seen = set()
        return len(roots) == 1 and is_valid_bt(roots.pop(), seen) and len(seen) == n
