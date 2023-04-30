class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: list[list[int]]) -> int:
        es = reduce(lambda a, x: a[x[0]].append((x[1], x[2])) or a, edges, ([], [], [], []))

        def union_count(dsu: DSU, es: Iterable[tuple[T, T]]) -> int:
            return sum(dsu.union(u, v) or 1 for u, v in es if not dsu.is_connected(u, v))

        xs = range(1, n + 1)
        a_dsu, b_dsu = DSU(xs), DSU(xs)
        used = sum((
            union_count(a_dsu, es[3]) and
            union_count(b_dsu, es[3]),
            union_count(a_dsu, es[1]),
            union_count(b_dsu, es[2]),
        ))

        return len(edges) - used if a_dsu.ds_count() == b_dsu.ds_count() == 1 else -1


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
