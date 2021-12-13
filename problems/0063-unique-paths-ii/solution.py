class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        dp = [0] * n
        prev = 1
        for i, j in product(range(m), range(n)):
            dp[j] = dp[j] + prev if grid[i][j] == 0 else 0
            prev = dp[j] if j < n - 1 else 0
        
        return dp[-1]
