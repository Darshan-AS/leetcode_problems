class Solution:
    def maxProbability(self, n: int, edges: list[list[int]], succ_prob: list[float], start: int, end: int) -> float:
        def max_probability(graph, start, end):
            max_prob = [0.0] * n
            max_prob[start] = 1.0
            
            pq = [(-1.0, start)]    
            while pq:
                cur_prob, cur_node = heapq.heappop(pq)
                if cur_node == end:
                    return -cur_prob
                for nxt_node, path_prob in graph[cur_node]:

                    if -cur_prob * path_prob > max_prob[nxt_node]:
                        max_prob[nxt_node] = -cur_prob * path_prob
                        heapq.heappush(pq, (-max_prob[nxt_node], nxt_node))
            return 0.0

        g = {i: [] for i in range(n)}
        for (u, v), p in zip(edges, succ_prob): g[u].append((v, p)); g[v].append((u, p))

        return max_probability(g, start, end)
