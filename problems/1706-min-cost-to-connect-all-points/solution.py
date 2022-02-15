class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:        
        # Kruskal's algorithm
        Edge = tuple[Any, Any, float]
        def minimum_spanning_tree(vertex_count: int, edges: Iterator[Edge]) -> Iterator[Edge]:
            dsu = DSU()
            pq = [(d, u, v) for u, v, d in edges]
            heapify(pq)

            while pq and vertex_count > 0:
                d, u, v = heappop(pq)
                if dsu.safe_is_connected(u, v): continue
                    
                dsu.safe_union(u, v)
                vertex_count -= 1
                yield (u, v, d)
        
        
        dist = lambda p1, p2: abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        
        n = len(points)
        connections = ((u, v, dist(points[u], points[v])) for u in range(n) for v in range(u, n))
        
        return sum(d for _, _, d in minimum_spanning_tree(n, connections))
    
class DSU:
    def __init__(self, xs: iter = None) -> None:
        self.parents = {x: x for x in xs} if xs else {}
        self.sizes = {x: 1 for x in xs} if xs else {}
    
    def add(self, x: Any) -> None:
        if x in self.parents: return
        self.parents[x] = x
        self.sizes[x] = 1
    
    def find(self, x: Any) -> Any:
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
        
    def union(self, u: Any, v: Any) -> None:
        ur = self.find(u)
        vr = self.find(v)
        
        low, high = (ur, vr) if self.sizes[ur] < self.sizes[vr] else (vr, ur)
        self.parents[low] = high
        self.sizes[high] += self.sizes[low]
    
    def is_connected(self, u: Any, v: Any) -> bool:
        ur = self.find(u)
        vr = self.find(v)
        return ur == vr
    
    def safe_find(self, x: Any) -> Any:
        self.add(x)
        return self.find(x)
    
    def safe_union(self, u: Any, v: Any) -> None:
        self.add(u)
        self.add(v)
        self.union(u, v)
    
    def safe_is_connected(self, u: Any, v: Any) -> bool:
        self.add(u)
        self.add(v)
        return self.is_connected(u, v)
            
        
