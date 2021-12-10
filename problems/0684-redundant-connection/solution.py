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
    
    def add(self, x: Any) -> None:
        if x in self.parents: return
        self.parents[x] = x
    
    def find_root(self, x: Any) -> Any:
        while self.parents[x] != x:
            x = self.parents[x]
        return x
        
    def union(self, u: Any, v: Any) -> None:
        ur = self.find_root(u)
        vr = self.find_root(v)
        
        self.parents[ur] = vr
    
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
        
