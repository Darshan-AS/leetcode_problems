class Solution:
    def minimumTime(self, time: list[int], total_trips: int) -> int:
        l, r = 0, min(time) * total_trips
        while l <= r:
            m = (l + r) // 2
            trips = sum(m // t for t in time)
            l, r = (l, m - 1) if trips >= total_trips else (m + 1, r)
        return l
