class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        return (t_ := iter(t)) and all(c in t_ for c in s)
