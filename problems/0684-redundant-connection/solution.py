class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        g = defaultdict(set)
        
        def connected(x, y, seen) -> bool:
            if x == y: return True
            seen.add(x)
            return any(connected(z, y, seen) for z in g[x] if z not in seen)
        
        for u, v in edges:
            if u in g and v in g and connected(u, v, set()):
                return [u, v]
            g[u].add(v)
            g[v].add(u)
        
