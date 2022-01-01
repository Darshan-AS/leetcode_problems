class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        
        dp = list(range(n + 1))
        prev = 0
        for i in range(m):
            prev, dp[0] = dp[0], dp[0] + 1
            for j in range(n):
                k = j + 1
                prev, dp[k] = dp[k], prev if word1[i] == word2[j] else min(prev, dp[k - 1], dp[k]) + 1
        
        return dp[-1]

