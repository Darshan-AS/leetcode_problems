class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        len1, len2 = len(word1), len(word2)
        
        dp = list(range(len2 + 1))
        
        for i in range(len1):
            prev = dp[0]
            dp[0] = prev + 1
            for j in range(len2):
                prev, dp[j + 1] = dp[j + 1], prev if word1[i] == word2[j] else min(dp[j] + 1, dp[j + 1] + 1, prev + 2)
                    
        return dp[-1]
