class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        def pairwise(iterable):
            a, b = tee(iterable)
            next(b, None)
            return zip(a, b)
        
        dsu = DSU()
        row_map, col_map = defaultdict(list), defaultdict(list)
        
        for x, y in stones:
            row_map[y].append((x, y))
            col_map[x].append((x, y))
        
        for ss in chain(row_map.values(), col_map.values()):
            for s1, s2 in pairwise(ss):
                dsu.safe_union(s1, s2)
        
        rem_stones = len(set(map(lambda s: dsu.safe_find_root(tuple(s)), stones)))
        return len(stones) - rem_stones
    
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
    
    def safe_find_root(self, x: Any) -> Any:
        self.add(x)
        return self.find_root(x)
    
    def safe_union(self, u: Any, v: Any) -> None:
        self.add(u)
        self.add(v)
        self.union(u, v)
    
    def safe_find(self, u: Any, v: Any) -> bool:
        self.add(u)
        self.add(v)
        return self.find(u, v)
