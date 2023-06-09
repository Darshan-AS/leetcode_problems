class Solution:
    def countNegatives(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        c = 0
        j = n - 1
        for i in range(m):
            while j >= 0 and grid[i][j] < 0: j -= 1
            c += n - j - 1
        return c
