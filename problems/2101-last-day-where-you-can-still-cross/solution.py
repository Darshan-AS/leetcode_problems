class Solution:
    def latestDayToCross(self, m: int, n: int, cells: list[list[int]]) -> int:
        LAND, WATER = 0, 1
        dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))
        grid = [[WATER] * n for _ in range(m)]

        in_bounds = lambda i, j: 0 <= i < m and 0 <= j < n
        nbrs = lambda i, j: ((i + di, j + dj) for di, dj in dirs)
        is_land = lambda i, j: grid[i][j] == LAND

        starfilter = lambda f, xs: filter(lambda args: f(*args), xs)

        sentinal_top, sentinal_bottom = (-inf, -inf), (inf, inf)
        norm_rcells =  map(lambda c: (c[0] - 1, c[1] - 1), reversed(cells))
        
        dsu = DSU(chain(product(range(m), range(n)), (sentinal_top, sentinal_bottom)))

        for k, (i, j) in enumerate(norm_rcells, 1):
            grid[i][j] = 0

            inbound_nbrs = starfilter(in_bounds, nbrs(i, j))
            land_nbrs = starfilter(is_land, inbound_nbrs)
            
            maybe_t = (sentinal_top,) if i == 0 else ()
            maybe_b = (sentinal_bottom,) if i == m - 1 else ()

            for nbr in chain(land_nbrs, maybe_t, maybe_b): dsu.union((i, j), nbr)
            if dsu.is_connected(sentinal_top, sentinal_bottom): return m * n - k
        
        return 0


class DSU:
    T = Hashable

    def __init__(self, xs: Iterable[T] = tuple()) -> None:
        self.parents, self.sizes = reduce(
            lambda a, x: setitem(a[0], x, x) or setitem(a[1], x, 1) or a,
            xs, ({}, {}),
        )
    
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
