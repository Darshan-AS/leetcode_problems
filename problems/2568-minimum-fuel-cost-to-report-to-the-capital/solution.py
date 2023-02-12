class Solution:
    def minimumFuelCost(self, roads: list[list[int]], seats: int) -> int:
        T = Hashable
        Graph = Mapping[T, Iterable[T]]

        def min_cost(graph: Graph, node: T, parent: T | None = None) -> tuple[int, int]:
            return reduce(
                lambda a, x: (a[0] + x[0] + ceil(x[1] / seats), a[1] + x[1]), 
                (min_cost(graph, child, node) for child in graph[node] if child != parent),
                (0, 1), # (total_cost, total_people)
            )
        
        g = defaultdict(list)
        for u, v in roads: g[u].append(v); g[v].append(u)

        return min_cost(g, 0)[0]
