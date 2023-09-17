class Solution:
    def shortestPathLength(self, graph: list[list[int]]) -> int:
        n = len(graph)
        all_nodes_mask = (1 << n) - 1
        seen_paths = set()

        @cache
        def shortest_path(node: int, path: int = 0) -> int:
            path |= 1 << node
            seen_paths.add((node, path))

            path_len = min((
                shortest_path(x, path)
                for x in graph[node]
                if (x, path) not in seen_paths
            ), default=inf) + 1 if path != all_nodes_mask else 0

            seen_paths.remove((node, path))
            return path_len
        
        return min(map(shortest_path, range(n)))
