class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        n = len(palindrome)
        if n == 1: return ""
        
        for i, ch in enumerate(palindrome[:n // 2]):
            if ch > 'a':
                return palindrome[:i] + 'a' + palindrome[i + 1:]
        
        return palindrome[:-1] + 'b'
