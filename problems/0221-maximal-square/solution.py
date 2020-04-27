class Solution:
    def maximalSquare(self, m: List[List[str]]) -> int:
        if not m:
            return 0
        
        dp = [0] * (len(m[0]) + 1)
        max_squares = 0

        for i in range(len(m)):
            cache = 0
            for j in range(len(m[0])):
                if m[i][j] == "1":
                    cache, dp[j + 1] = dp[j + 1], min(dp[j], dp[j + 1], cache) + 1
                    max_squares = max(max_squares, dp[j + 1])
                else:
                    dp[j + 1] = 0            
                    
        return max_squares ** 2
                    
