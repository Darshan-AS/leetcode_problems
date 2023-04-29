class Solution:
    def distanceLimitedPathsExist(self, n: int, edges: list[list[int]], queries: list[list[int]]) -> list[bool]:
        s_edges = sorted(edges, key=itemgetter(2))
        s_queries = sorted(enumerate(queries), key=lambda x: x[1][2])

        dsu = DSU(range(n))
        ans = [False] * len(queries)
        i = 0
        for j, (u, v, k) in s_queries:
            while i < len(s_edges) and s_edges[i][2] < k:
                dsu.union(s_edges[i][0], s_edges[i][1])
                i += 1
            ans[j] = dsu.is_connected(u, v)
        
        return ans


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
