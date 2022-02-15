class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:        
        Graph = dict[Any, list[Any, float]]
        Edge = tuple[Any, Any, float]
        
        # Prim's algorithm
        def minimum_spanning_tree(graph: Graph) -> Iterator[Edge]:
            if not graph:
                return

            u = next(iter(graph))
            seen = {u}
            pq = [(d, u, v) for v, d in graph[u]]
            heapify(pq)

            while pq and len(seen) < len(graph):
                d, u, v = heappop(pq)
                if v in seen:
                    continue

                for v_, d_ in graph[v]:
                    if v_ not in seen:
                        heappush(pq, (d_, v, v_))

                seen.add(v)
                yield (u, v, d)
        
        
        dist = lambda p1, p2: abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        
        n = len(points)
        connections = ((u, v, dist(points[u], points[v])) for u in range(n) for v in range(u, n))
        
        graph_ = defaultdict(list)
        for u, v, d in connections:
            graph_[u].append((v, d))
            graph_[v].append((u, d))
        
        return sum(d for _, _, d in minimum_spanning_tree(graph_))

