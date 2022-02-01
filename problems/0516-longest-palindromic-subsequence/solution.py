class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        
        dp = [0] * (n + 1)
        for i, j in product(range(n), range(n - 1, -1, -1)):
            k = j
            prev = dp[n] if j == n - 1 else prev
            prev, dp[k] = dp[k], prev + 1 if s[i] == s[j] else max(dp[k + 1], dp[k])

        return dp[0]
