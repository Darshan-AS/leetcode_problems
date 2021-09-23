class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        n = len(palindrome)
        
        for i, ch in enumerate(palindrome[:n // 2]):
            if ch > 'a':
                return palindrome[:i] + 'a' + palindrome[i + 1:]
        
        return palindrome[:-1] + 'b' if n > 1 else ""
