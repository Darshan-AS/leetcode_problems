class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        dp = [math.inf] * (n + 1)
        dp[1] = 0
        for i, j in product(range(m), range(n)):
            k = j + 1
            dp[k] = min(dp[k - 1], dp[k]) + grid[i][j]
        
        return dp[-1]
