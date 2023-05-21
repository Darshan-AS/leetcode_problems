class Solution:
    def shortestBridge(self, grid: list[list[int]]) -> int:
        def is_valid(x):
            return 0 <= x[0] < len(grid) and 0 <= x[1] < len(grid)
        
        def valid_nbrs(x):
            return filter(is_valid, ((x[0] + di, x[1] + dj) for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1))))
        
        def is_boundary(x, k, seen):
            return grid[x[0]][x[1]] == k and any(grid[ni][nj] != k for ni, nj in valid_nbrs(x) if (ni, nj) not in seen)
        
        def foo(ys, k):
            level = tuple(ys)
            seen = set(level)
            while level:
                bs = []
                level = tuple(
                    seen.add(x) or x
                    for i, j in level
                    if not (bs.append((i, j)) if is_boundary((i, j), k, seen) else None)
                    for x in valid_nbrs((i, j))
                    if x not in seen
                    and grid[x[0]][x[1]] == k
                )
                yield bs
        
        
        n = len(grid)
        a = next((i, j) for i, j in product(range(n), range(n)) if grid[i][j])

        xs = list(foo((a,), 1))
        ys = list(foo(chain.from_iterable(xs), 0))
        return next(i for i, y in enumerate(ys) if y)
