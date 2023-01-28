class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        words = set(wordDict)
        n = len(s)
        
        dp = [False] * (n + 1)
        dp[0] = True
        
        for j in range(1, n + 1):
            dp[j] = any(dp[i] and s[i:j] in words for i in range(j))
        
        return dp[n]
