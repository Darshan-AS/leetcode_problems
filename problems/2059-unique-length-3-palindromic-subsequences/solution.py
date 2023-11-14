class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        ranges = {}
        for r, x in enumerate(s):
            l = ranges.get(x, (r, r))[0]
            ranges[x] = (l, r)
        
        return sum(len(set(s[l + 1 : r])) for l, r in ranges.values())
