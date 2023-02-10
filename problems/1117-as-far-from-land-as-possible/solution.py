class Solution:
    def maxDistance(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        dp = [[inf for _ in range(n + 2)] for _ in range(m + 2)]

        # Top-Left to Bottom-Right
        for i_, j_ in product(range(m), range(n)):
            i, j = i_ + 1, j_ + 1
            dp[i][j] = 0 if grid[i_][j_] else min(dp[i][j], dp[i - 1][j] + 1, dp[i][j - 1] + 1)
        
        # Bottom-Right to Top-Left
        for i_, j_ in product(range(m - 1, -1, -1), range(n - 1, -1, -1)):
            i, j = i_ + 1, j_ + 1
            dp[i][j] = 0 if grid[i_][j_] else min(dp[i][j], dp[i + 1][j] + 1, dp[i][j + 1] + 1)
        
        d = max(dp[i + 1][j + 1] for i, j in product(range(m), range(n)))
        return -1 if d in (0, inf) else d
