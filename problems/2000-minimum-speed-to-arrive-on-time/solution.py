class Solution:
    def minSpeedOnTime(self, dist: list[int], hour: float) -> int:
        n = len(dist)
        if hour <= n - 1: return -1

        l = int(max(sum(dist) // hour, 1))
        r = int(max(max(dist), dist[-1] / (hour - (n - 1)))) + 1

        while l < r:
            m = (l + r) // 2
            ds = reversed(dist)
            t = sum((ceil(d / m) for d in ds), next(ds) / m)
            l, r = (l, m) if t < hour or isclose(t, hour, rel_tol=1e-12) else (m + 1, r)
        
        return int(l)
