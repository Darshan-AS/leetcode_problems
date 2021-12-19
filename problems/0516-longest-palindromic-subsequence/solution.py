class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        s1, s2 = s, s[-1::-1]
        
        dp = [0] * (n + 1)
        for i, j in product(range(n), range(n)):
            k = j + 1
            prev = dp[0] if j == 0 else prev
            prev, dp[k] = dp[k], prev + 1 if s1[i] == s2[j] else max(dp[k - 1], dp[k])

        return dp[-1]
