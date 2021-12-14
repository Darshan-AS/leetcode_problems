class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        len1, len2 = len(s1), len(s2)
        
        dp = list(accumulate((ord(ch) for ch in s2), initial=0))
        
        for i in range(len1):
            prev = dp[0]
            dp[0] = prev + ord(s1[i])
            
            for j in range(len2):
                prev, dp[j + 1] = dp[j + 1], (
                    prev
                    if s1[i] == s2[j] else 
                    min(dp[j + 1] + ord(s1[i]), dp[j] + ord(s2[j]))
                )
                                
        return dp[-1]
