class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        dp = [math.inf] * n
        prev = 0
        for i, j in product(range(m), range(n)):
            dp[j] = min(dp[j], prev) + grid[i][j]
            prev = dp[j] if j < n - 1 else math.inf
        
        return dp[-1]
