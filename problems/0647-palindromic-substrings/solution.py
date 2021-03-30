class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        count = n
        dp = [[False] * n for _ in range(n)]
        
        for i in range(n):
            dp[i][i] = True
            
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
            count += dp[i][i + 1]
        
        for length in range(3, n + 1):
            i, j = 0, length - 1
            while j < n:
                dp[i][j] = dp[i + 1][j - 1] and s[i] == s[j]
                count += dp[i][j]
                i += 1
                j += 1
                
        return count
