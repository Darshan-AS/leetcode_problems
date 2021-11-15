class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand_palindrome(start: int, end: int) -> tuple[int, int]:
            i, j = start, end
            while i >= 0 and j < len(s) and s[i] == s[j]:
                i, j = i - 1, j + 1
            return i + 1, j - 1
        
        i, j = max(
            chain.from_iterable(
                (expand_palindrome(i, i), expand_palindrome(i, i + 1))
                for i in range(len(s))
            ),
            key=lambda x: x[1] - x[0],
        )
        
        return s[i: j + 1]
