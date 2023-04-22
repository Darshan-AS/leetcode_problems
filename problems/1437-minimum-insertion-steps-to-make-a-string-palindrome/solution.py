class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            prev = dp[i]
            for j in range(i + 1, n):
                k = j + 1
                prev, dp[k] = (dp[k], prev if s[i] == s[j] else 1 + min(dp[k - 1], dp[k]))
        return dp[-1]
