class Solution:
    def numDecodings(self, s: str) -> int:        
        n = len(s)
        dp = [0, 1] + [0] * n
        for x in range(n):
            i = x + 2
            
            dp[i] = (
                (dp[i - 1] if int(s[x]) else 0) +
                (dp[i - 2] if x > 0 and int(s[x - 1]) and int(s[x - 1: x + 1]) <= 26 else 0)
            )
        
        return dp[-1]
