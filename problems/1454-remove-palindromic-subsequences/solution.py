class Solution:
    def removePalindromeSub(self, s: str) -> int:
        return (s != '') + (s != s[::-1])
