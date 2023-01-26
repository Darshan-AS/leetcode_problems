class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        T = Hashable
        W = int | float
        WeightedGraph = defaultdict[T, defaultdict[T, W]]

        def shortest_weight_dijkstras(graph: WeightedGraph, src: T, dst: T, k_: int=math.inf) -> W:
            pq = [(0, src, k_)]
            visited_at = defaultdict(int)
            while pq:
                w, u, k = heapq.heappop(pq)
                if u == dst: return w
                if visited_at[u] >= k: continue
                visited_at[u] = k
                for v, dw in graph[u].items(): heapq.heappush(pq, (w + dw, v, k - 1))
            return math.inf
        
        g = defaultdict(lambda: defaultdict(int))
        for from_, to, price in flights: g[from_][to] = price
        
        price = shortest_weight_dijkstras(g, src, dst, k + 1)
        return -1 if price == math.inf else price
