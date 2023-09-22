class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        return len(s) in accumulate(t, lambda i, x: i + (s[i] == x), initial=0)

