from collections.abc import *

class Solution:
    def countSubTrees(self, n: int, edges: list[list[int]], labels_: str) -> list[int]:
        T = TypeVar('T')
        Tree = Mapping[T, Collection[T]]
        Label = str

        def count_sub_trees(tree: Tree, labels: Sequence[Label], root_: T, parent_: T) -> Sequence[int]:
            ans = list(range(n))

            def count_labels(root: T, parent: T) -> Counter[Label]:
                c = reduce(
                    lambda a, x: a.update(x) or a,
                    (count_labels(child, root) for child in tree[root] if child != parent),
                    Counter(labels[root]),
                )
                ans[root] = c[labels[root]]
                return c

            count_labels(root_, parent_)
            return ans

        t = defaultdict(list)
        for u, v in edges: t[u].append(v); t[v].append(u)

        return count_sub_trees(t, labels_, 0, -1)

