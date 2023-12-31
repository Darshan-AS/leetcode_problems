class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        d = defaultdict(lambda: (-inf, inf))
        for i, x in enumerate(s): d[x] = (max(d[x][0], i), min(d[x][1], i))
        return max(starmap(sub, d.values())) - 1
