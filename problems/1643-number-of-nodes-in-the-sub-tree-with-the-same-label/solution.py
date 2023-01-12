class Solution:
    def countSubTrees(self, n: int, edges: list[list[int]], labels: str) -> list[int]:

        def count_sub_trees(n: int, tree: dict[int, list[int]], labels: str) -> list[int]:
            ans = list(range(n))
            counter = Counter()

            def count_labels(root: int, parent: int) -> None:
                before = counter[labels[root]]

                for child in tree[root]:
                    if child != parent: count_labels(child, root) 
                counter[labels[root]] += 1

                after = counter[labels[root]]
                ans[root] = after - before

            count_labels(0, -1)
            return ans

        t = defaultdict(list)
        for u, v in edges: t[u].append(v); t[v].append(u)

        return count_sub_trees(n, t, labels)

