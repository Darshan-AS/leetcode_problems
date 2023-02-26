class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        w1, w2 = (word1, word2) if len(word1) < len(word2) else (word2, word1)
        n1, n2 = len(w1), len(w2)

        dp = list(range(n1 + 1))
        for i in range(n2):
            prev, dp[0] = dp[0], dp[0] + 1
            for j in range(n1):
                k = j + 1
                prev, dp[k] = dp[k], prev if w1[j] == w2[i] else min(prev, dp[k - 1], dp[k]) + 1
        
        return dp[-1]
