class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        
        dp = list(range(n + 1))
        prev = 0
        for i in range(m):
            prev, dp[0] = dp[0], dp[0] + 1
            for j in range(n):
                prev, dp[j + 1] = dp[j + 1], prev if word1[i] == word2[j] else min(prev, dp[j + 1], dp[j]) + 1
        
        return dp[-1]

