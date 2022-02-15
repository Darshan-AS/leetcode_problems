class Solution:
    def makeConnected(self, n: int, connections: list[list[int]]) -> int:
        if len(connections) < n - 1: return -1
        
        graph = defaultdict(list)
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)
        
        def visit_from(g: dict, root: int, seen: set) -> None:
            if root in seen: return
            seen.add(root)
            for node in g[root]: visit_from(g, node, seen)
        
        visited = set()
        ds_count = 0
        for u in range(n):
            if u not in visited:
                ds_count += 1
                visit_from(graph, u, visited)
            
        return ds_count - 1

