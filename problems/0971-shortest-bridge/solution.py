class Solution:
    def shortestBridge(self, grid: list[list[int]]) -> int:
        Pos = tuple[int, int]
        Val = Literal[1, 0]

        n = len(grid)

        def get(x: Pos) -> Val:
            return grid[x[0]][x[1]]
        
        def is_valid(x: Pos) -> bool:
            return 0 <= x[0] < n and 0 <= x[1] < n
        
        def valid_nbrs(x: Pos) -> Iterator[Pos]:
            return filter(is_valid, ((x[0] + d0, x[1] + d1) for d0, d1 in ((1, 0), (0, 1), (-1, 0), (0, -1))))
        
        def is_boundary(x: Pos, k: Val, skips: set[Pos]) -> bool:
            return get(x) == k and any(get(nbr) != k for nbr in valid_nbrs(x) if nbr not in skips)
        
        def level_order_boundaries(xs: Iterable[Pos], k: Val) -> Iterator[tuple[Pos]]:
            level = set(xs)
            seen = set()
            while level:
                seen.update(level)
                yield tuple(l for l in level if is_boundary(l, k, seen))
                level = set(nbr
                    for l in level for nbr in valid_nbrs(l)
                    if nbr not in seen and get(nbr) == k
                )
        
        land = next((i, j) for i, j in product(range(n), range(n)) if grid[i][j])
        island1_boundaries = level_order_boundaries((land,), 1)
        island2_boundaries = level_order_boundaries(chain.from_iterable(island1_boundaries), 0)
        return next(i for i, y in enumerate(island2_boundaries) if y)
