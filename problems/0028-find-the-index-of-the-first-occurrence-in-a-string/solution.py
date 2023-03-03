class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack) - len(needle) + 1):
            if all(haystack[i + j] == needle[j] for j in range(len(needle))):
                return i
        return -1
