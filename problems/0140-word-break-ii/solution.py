class Solution:
    def wordBreak(self, s: str, words: list[str]) -> list[str]:
        words_set = set(words)        
        n = len(s)
        
        dp = [[] for _ in range (n + 1)]
        dp[0] = ['']
        
        for j in range(1, n + 1):
            dp[j] = list(chain.from_iterable(
                (p + ' ' + ss if p else ss for p in dp[i])
                for i in range(j)
                if (ss := s[i:j]) in words_set
            ))
        
        return dp[-1]
