class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def enclosed(i: int, j: int) -> bool:
            if i < 0 or j < 0 or i >= m or j >= n: return - (m * n)
            if grid[i][j] == 0: return 0
            grid[i][j] = 0
            return 1 + sum(enclosed(i + di, j + dj) for di, dj in ((0, -1), (0, 1), (-1, 0), (1, 0)))

        return sum(max(enclosed(i, j), 0) for i, j in product(range(m), range(n)) if grid[i][j] == 1)

