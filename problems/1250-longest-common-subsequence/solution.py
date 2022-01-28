class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1, n2 = len(text1), len(text2)
        
        dp = [0] * (n2 + 1)
        
        for i, j in product(range(n1), range(n2)):
            k = j + 1
            prev = dp[0] if j == 0 else prev
            prev, dp[k] = dp[k], prev + 1 if text1[i] == text2[j] else max(dp[k - 1], dp[k])
                    
        return dp[-1]
