class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        idxs = defaultdict(list)
        for i, x in enumerate(t): idxs[x].append(i)

        i = 0
        for ch in s:
            idx = bisect_left(idxs[ch], i)
            if idx >= len(idxs[ch]): return False
            i = idxs[ch][idx] + 1
        return True

