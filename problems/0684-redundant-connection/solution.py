class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        dsu = DSU()
        for u, v in edges:
            if dsu.safe_find(u, v):
                return [u, v]
            dsu.safe_union(u, v)
    
class DSU:
    def __init__(self, xs: iter = None) -> None:
        self.parents = {x: x for x in xs} if xs else {}
        self.sizes = {x: 1 for x in xs} if xs else {}
    
    def add(self, x: Any) -> None:
        if x in self.parents: return
        self.parents[x] = x
        self.sizes[x] = 1
    
    def find_root(self, x: Any) -> Any:
        if self.parents[x] != x:
            self.parents[x] = self.find_root(self.parents[x])
        return self.parents[x]
        
    def union(self, u: Any, v: Any) -> None:
        ur = self.find_root(u)
        vr = self.find_root(v)
        
        low, high = (ur, vr) if self.sizes[ur] < self.sizes[vr] else (vr, ur)
        self.parents[low] = high
        self.sizes[high] += self.sizes[low]
    
    def find(self, u: Any, v: Any) -> bool:
        ur = self.find_root(u)
        vr = self.find_root(v)
        return ur == vr
    
    def safe_union(self, u: Any, v: Any) -> None:
        self.add(u)
        self.add(v)
        self.union(u, v)
    
    def safe_find(self, u: Any, v: Any) -> bool:
        self.add(u)
        self.add(v)
        return self.find(u, v)
        
