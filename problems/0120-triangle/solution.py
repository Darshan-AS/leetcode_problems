class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # Top down iterative DP
        
        dp = (0, 0)
        for i in range(len(triangle)):
            dp = (math.inf, *(min(dp[j], dp[j + 1]) + triangle[i][j] for j in range(i + 1)), math.inf)
        
        return min(dp)
