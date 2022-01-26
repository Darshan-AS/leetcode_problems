class Solution:
    def longestPalindrome(self, s: str) -> int:
        even_len = sum(c & ~1 for c in Counter(s).values())
        return even_len + (even_len < len(s))
