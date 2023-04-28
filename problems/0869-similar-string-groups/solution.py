class Solution:
    def numSimilarGroups(self, strs: list[str]) -> int:
        is_similar = lambda s1, s2: sum(map(ne, s1, s2)) in (0, 2)
        splat = lambda f: lambda args: f(*args)
        
        pairs = filter(splat(is_similar), product(strs, strs))

        dsu = DSU(strs)
        for s1, s2 in pairs: dsu.union(s1, s2)
        return dsu.ds_count()


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
        if ur == vr:
            return
        low, high = (ur, vr) if self.sizes[ur] < self.sizes[vr] else (vr, ur)
        self.parents[low] = high
        self.sizes[high] += self.sizes[low]
        self.count -= 1

    def is_connected(self, u: T, v: T) -> bool:
        return self.find(u) == self.find(v)

    def ds_count(self) -> int:
        return self.count
