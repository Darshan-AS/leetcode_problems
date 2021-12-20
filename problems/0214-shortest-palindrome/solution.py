class Solution:
    def shortestPalindrome(self, s: str) -> str:
        n = len(s)
        i, j = 0, len(s) - 1
        
        while j >= 0:
            if s[i] == s[j]: i += 1
            j -= 1
        
        if i == n: return s
        
        # The shortest palindrome must be in s[0:i]
        return s[n - 1: i - 1: -1] + self.shortestPalindrome(s[:i]) + s[i:]
