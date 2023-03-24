class Solution:
    def minReorder(self, n: int, connections: list[list[int]]) -> int:
        T = Hashable
        Direction = bool
        Graph = Mapping[T, Iterable[tuple[T, Direction]]]

        def min_flips(graph: Graph, u: T, parent: T | None = None) -> int:
            return sum(min_flips(graph, v, u) + d for v, d in graph[u] if v != parent)

        g = defaultdict(list)
        for u, v in connections: g[u].append((v, True)); g[v].append((u, False))
        return min_flips(g, 0)

