class Solution:
    def isBipartite(self, graph: list[list[int]]) -> bool:
        n = len(graph)
        
        def dfs_groupify(node, ga, gb):
            if node in gb: return False
            if node in ga: return True
            ga.add(node)
            return all(dfs_groupify(child, gb, ga) for child in graph[node])
                
        
        group_a, group_b = set(), set()
        return all(
            u in group_a or u in group_b or dfs_groupify(u, group_a, group_b)
            for u in range(n)
        )

