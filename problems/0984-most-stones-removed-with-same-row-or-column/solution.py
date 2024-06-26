class Solution:
    def removeStones(self, stones: list[list[int]]) -> int:        
        dsu = DSU()
        row_map, col_map = defaultdict(list), defaultdict(list)
        
        for x, y in stones:
            row_map[y].append((x, y))
            col_map[x].append((x, y))
        
        for ss in chain(row_map.values(), col_map.values()):
            for s1, s2 in pairwise(ss):
                dsu.union(s1, s2)
        
        rem_stones = len(set(dsu.find(tuple(s)) for s in stones))
        return len(stones) - rem_stones


class DSU:
    T = Hashable

    def __init__(self, xs: Iterable[T] = tuple()) -> None:
        self.parents = {x: x for x in xs}
        self.sizes = {x: 1 for x in xs}
    
    def add(self, x: T) -> None:
        if x in self.parents: return
        self.parents[x] = x
        self.sizes[x] = 1
    
    def make_safe(func: Callable) -> Callable:
        """Decorator used to ensure input values are added to parents using in func"""
        def wrapper(self, *xs):
            for x in xs: self.add(x)
            return func(self, *xs)
        return wrapper
    
    @make_safe
    def union(self, u: T, v: T) -> None:
        ur, vr = self.find(u), self.find(v)
        short_t, long_t = (ur, vr) if self.sizes[ur] < self.sizes[vr] else (vr, ur)

        self.parents[short_t] = long_t
        self.sizes[long_t] += self.sizes[short_t]
    
    @make_safe
    def find(self, x: T) -> T:
        self.parents[x] = self.find(self.parents[x]) if self.parents[x] != x else x
        return self.parents[x]
    
    @make_safe
    def is_connected(self, u: T, v: T) -> bool:
        return self.find(u) == self.find(v)
