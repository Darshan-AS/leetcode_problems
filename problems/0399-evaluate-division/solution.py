class Solution:
    def calcEquation(self, equations: list[list[str]], values: list[float], queries: list[list[str]]) -> list[float]:
        T = Hashable
        W = int | float
        WeightedGraph = Mapping[T, Mapping[T, W]]
        def solve_div(graph: WeightedGraph, src: T, dest: T, seen: set[T]) -> W:
            seen.add(src)
            q = next((
                graph[src][v] * x
                for v in graph[src]
                if v not in seen and
                (x := solve_div(graph, v, dest, seen)) != -1
            ), -1) if src != dest else 1
            seen.remove(src)
            return q
        
        g = defaultdict(lambda: defaultdict(int))
        for (n, d), v in zip(equations, values): g[n][d] = v; g[d][n] = 1 / v

        return [solve_div(g, s, d, set()) if s in g and d in g else -1 for s, d in queries]
