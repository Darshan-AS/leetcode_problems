class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = {node: set() for node in range(n)}
        
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
        
        while (level := [u for u, vs in graph.items() if len(vs) == 1]) and len(graph) > 2:
            for u in level:
                for v in graph[u]:
                    graph[v].remove(u)
                del graph[u]
        
        return graph.keys()
            
