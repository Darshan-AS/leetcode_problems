class Solution:
    def minDifficulty(self, jobs: List[int], d: int) -> int:
        n = len(jobs)        
        dp = [[-1] * (n + 1) for _ in range(d + 1)]
        
        for i in range(1, n + 1):
            dp[1][i] = max(dp[1][i - 1], jobs[i - 1])
        
        for i in range(2, d + 1):
            for j in range(i, n + 1):
                dp[i][j] = min(dp[i - 1][k] + max(jobs[k:j]) for k in range(i - 1, j))
        
        return dp[d][n]
