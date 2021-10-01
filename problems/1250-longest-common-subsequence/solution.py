class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        len1, len2 = len(text1), len(text2)
        
        dp = [0] * (len2 + 1)
        
        for i in range(len1):
            prev = dp[0]
            for j in range(len2):
                prev, dp[j + 1] = dp[j + 1], prev + 1 if text1[i] == text2[j] else max(dp[j], dp[j + 1])
                    
        return dp[-1]
