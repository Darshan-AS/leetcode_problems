class Solution:
    def makeConnected(self, n: int, connections: list[list[int]]) -> int:
        if len(connections) < n - 1: return -1

        dsu = DSU(range(n))
        for u, v in connections: dsu.union(u, v)
        return dsu.ds_count() - 1

T = Hashable
class DSU:
    def __init__(self, xs: Iterable[T] = ()) -> None:
        self.parents: Mapping[T, T] = {x: x for x in xs}
        self.sizes: Mapping[T, int] = {x: 1 for x in xs}
        self.count: int = len(self.parents)

    def find(self, u: T) -> T:
        self.parents[u] = u if self.parents[u] == u else self.find(self.parents[u])
        return self.parents[u]
    
    def union(self, u: T, v: T) -> None:
        ur, vr = self.find(u), self.find(v)
        if ur == vr: return
        low, high = (ur, vr) if self.sizes[ur] < self.sizes[vr] else (vr, ur)
        self.parents[low] = high
        self.sizes[high] += self.sizes[low]
        self.count -= 1
    
    def is_connected(self, u: T, v: T) -> bool:
        return self.find(u) == self.find(v)
    
    def ds_count(self) -> int:
        return self.count
    
    def add(self, u: T) -> None:
        if u in self.parents: return
        self.parents[u] = u
        self.sizes[u] = 1
        self.count += 1
    
    def safe_find(self, u: T) -> T:
        self.add(u)
        return self.find(u)
    
    def safe_union(self, u: T, v: T) -> None:
        self.add(u); self.add(v)
        self.union(u, v)
    
    def safe_is_connected(self, u: T, v: T) -> bool:
        self.add(u); self.add(v)
        return self.is_connected(u, v)
