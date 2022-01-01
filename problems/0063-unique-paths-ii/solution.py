class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        dp = [0] * (n + 1)
        dp[1] = 1
        for i, j in product(range(m), range(n)):
            k = j + 1
            dp[k] = dp[k - 1] + dp[k] if grid[i][j] == 0 else 0
        
        return dp[-1]
