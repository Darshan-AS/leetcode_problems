class Solution:
    def minDeletions(self, s: str) -> int:
        xs = Counter(s).values()
        seen = set()
        c = 0
        for x in xs:
            y = next((k for k in range(x, -1, -1) if k not in seen), 0)
            c += x - y
            seen.add(y)
        return c
