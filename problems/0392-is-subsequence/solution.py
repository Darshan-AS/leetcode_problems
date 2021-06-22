from collections import defaultdict
from bisect import bisect_left

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        indices_map = defaultdict(list)
        for i, ch in enumerate(t):
            indices_map[ch].append(i)
        
        start = 0
        for ch in s:
            ch_indicies = indices_map[ch]
            index = bisect_left(ch_indicies, start)
            if index >= len(ch_indicies):
                return False
            start = ch_indicies[index] + 1
        return True
