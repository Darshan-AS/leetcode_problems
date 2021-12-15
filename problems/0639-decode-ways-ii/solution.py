class Solution:
    def numDecodings(self, s: str) -> int:
        M = 1_000_000_007
        
        n = len(s)
        dp = [0, 1] + [0] * n
        
        for x in range(n):
            i = x + 2
            
            prev_ch, ch = s[x - 1] if x else '0', s[x]
            
            if ch == '*':
                dp[i] = (dp[i - 1] * 9) % M
                if prev_ch == '1':
                    dp[i] = (dp[i] + dp[i - 2] * 9) % M
                elif prev_ch == '2':
                    dp[i] = (dp[i] + dp[i - 2] * 6) % M
                elif prev_ch == '*':
                    dp[i] = (dp[i] + dp[i - 2] * 15) % M
            else:
                dp[i] = dp[i - 1] if ch != '0' else 0
                if prev_ch == '1':
                    dp[i] = (dp[i] + dp[i - 2]) % M
                elif prev_ch == '2':
                    dp[i] = (dp[i] + dp[i - 2] * (1 if ch <= '6' else 0)) % M
                elif prev_ch == '*':
                    dp[i] = (dp[i] + dp[i - 2] * (2 if ch <= '6' else 1)) % M
        
        return dp[-1]
