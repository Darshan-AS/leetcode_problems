class Solution:
    def isBipartite(self, graph: list[list[int]]) -> bool:
        T = Hashable
        def is_bi(u: T, ga: set[T], gb: set[T]) -> bool:
            return u not in gb and (ga.add(u) or all(is_bi(v, gb, ga) for v in graph[u] if v not in gb))
        
        
        group_a, group_b = set(), set()
        return all(u in group_a or u in group_b or is_bi(u, group_a, group_b) for u in range(len(graph)))
