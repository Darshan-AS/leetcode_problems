class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        
        dp = [0] * (n + 1) # -1 index out of bound is handled by dp[-1]
        
        for i in range(1, n):
            if s[i] == '(':                                                     # '.........('
                dp[i] == 0
            elif s[i - 1] == '(':                                               # '........()'
                dp[i] = dp[i - 2] + 2
            elif (i - 1) - dp[i - 1] >= 0 and s[(i - 1) - dp[i - 1]] == '(':    # '..((....))'
                dp[i] = dp[i - 1] + dp[(i - 1) - dp[i - 1] - 1] + 2
                    
        return max(dp)
