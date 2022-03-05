class Solution:
    def getAncestors(self, n: int, edges: list[list[int]]) -> list[list[int]]:
        r_graph = {i: list() for i in range(n)}
        for u, v in edges: r_graph[v].append(u)
        
        @cache
        def find_ancestors(node: int) -> Iterator[int]:
            ancestors = set(r_graph[node])
            for a in r_graph[node]: ancestors.update(find_ancestors(a))
            return ancestors
        
        return list(sorted(find_ancestors(node)) for node in r_graph)
