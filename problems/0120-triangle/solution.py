class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:     
        n = len(triangle)
        
        dp = [math.inf] * (n + 1)
        dp[1] = 0
        for i in range(n):
            prev = dp[0]
            for j in range(i + 1):
                k = j + 1
                prev, dp[k] = dp[k], min(prev, dp[k]) + triangle[i][j]
        
        return min(dp)
