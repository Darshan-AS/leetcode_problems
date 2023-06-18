class Solution:
    def countPaths(self, grid: list[list[int]]) -> int:
        M = 1_000_000_007
        m, n = len(grid), len(grid[0])
        dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))

        in_bounds = lambda i, j: 0 <= i < m and 0 <= j < n
        nbrs = lambda i, j: ((i + di, j + dj) for di, dj in dirs)
        starfilter = lambda f, xs: filter(lambda args: f(*args), xs)

        @cache
        def paths_to(i: int, j: int) -> int:
            valid_nbrs = starfilter(in_bounds, nbrs(i, j))
            increasing_nbrs = starfilter(lambda ni, nj: grid[ni][nj] > grid[i][j], valid_nbrs)
            return (sum(starmap(paths_to, increasing_nbrs)) + 1) % M
        
        return sum(starmap(paths_to, product(range(m), range(n)))) % M
