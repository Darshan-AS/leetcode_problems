class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        n = len(s)
        
        dp = [False] * (n + 1)
        dp[0] = True
        for j in range(n + 1):
            for i in range(j):
                if dp[i] and s[i:j] in words:
                    dp[j] = True
                    break
        return dp[-1]
