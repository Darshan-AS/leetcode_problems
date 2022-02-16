class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        Graph = dict[Any, list[Any, float]]
        Dist = tuple[Any, Any, float]
        
        # Dijkstra's Algorithm
        def shortest_paths(graph: Graph, s: Any) -> Iterator[Dist]:
            if not graph:
                return

            seen = set()
            pq = [(0, s)]
            pq.extend(((math.inf, u) for u in graph))

            while pq and len(seen) < len(graph):
                d, v = heappop(pq)
                if v in seen:
                    continue

                for v_, d_ in graph[v]:
                    heappush(pq, (d + d_, v_))

                seen.add(v)
                yield (s, v, d)
        
        graph_ = {u: list() for u in range(1, n + 1)}
        for u, v, d in times:
            graph_[u].append((v, d))
        
        max_time = max(d for _, _, d in shortest_paths(graph_, k))
        return max_time if max_time != math.inf else -1
