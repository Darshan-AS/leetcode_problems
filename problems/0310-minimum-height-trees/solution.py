class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = {node: set() for node in range(n)}
        
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
        
        leaves = [u for u, vs in graph.items() if len(vs) == 1]
        while len(graph) > 2:
            new_leaves = []
            for u in leaves:
                v = graph[u].pop() # only 1 connection in any leaf
                graph[v].remove(u)
                if len(graph[v]) == 1: new_leaves.append(v)
                del graph[u]
            leaves = new_leaves
        
        return graph.keys()
            
