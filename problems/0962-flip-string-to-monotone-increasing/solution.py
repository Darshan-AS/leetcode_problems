from itertools import accumulate


class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        n = len(s)
        counts = tuple(accumulate(s, lambda c, ch: c + (ch == "1"), initial=0))

        return min(map(lambda x: counts[x] + ((n - x) - (counts[-1] - counts[x])), range(n + 1)))

