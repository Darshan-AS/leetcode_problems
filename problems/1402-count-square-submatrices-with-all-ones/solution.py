class Solution:
    def countSquares(self, a: List[List[int]]) -> int:
        m, n = len(a), len(a[0])
        
        count = 0
        dp = [0] * (n + 1)
        prev = 0
        for i in range(m):
            for j in range(n):
                old_prev, prev = prev, dp[j + 1]
                dp[j + 1] = min(dp[j], dp[j + 1], old_prev) + 1 if a[i][j] else 0
            count += sum(dp)
            
        return count
        
