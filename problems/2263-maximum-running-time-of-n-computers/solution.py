class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        l, r = 1, sum(batteries) // n
        while l < r:
            m = ceil((r + l) / 2)
            extra = sum(map(min, batteries, repeat(m)))
            l, r = (m, r) if extra // n >= m else (l, m - 1)
        return l
