class Solution:
    def uniquePathsWithObstacles(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])

        npaths = [0] * (n + 1)
        npaths[1] = 1

        for i, j in product(range(m), range(n)):
            npaths[j + 1] = 0 if grid[i][j] else npaths[j + 1] + npaths[j]
        
        return npaths[-1]
