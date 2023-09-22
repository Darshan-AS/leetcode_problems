class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        for x in t:
            if i >= len(s): return True
            i += (s[i] == x)
        return i >= len(s)
