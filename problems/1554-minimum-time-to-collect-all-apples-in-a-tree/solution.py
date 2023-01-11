from collections.abc import *

class Solution:
    def minTime(self, n: int, edges: list[list[int]], hasApple: list[bool]) -> int:
        T = TypeVar('T')
        Tree = Mapping[T, Collection[T]]

        def collect_apples(
            tree: Tree, has_apples: Sequence[bool], root: T, parent: T
        ) -> tuple[int, bool]:
            return sum(
                (c := collect_apples(tree, has_apples, child, root))
                + 2 * bool(c or has_apples[child])
                for child in tree[root]
                if child != parent
            )

        t = defaultdict(list)
        for u, v in edges: t[u].append(v); t[v].append(u)

        return collect_apples(t, hasApple, 0, -1)
