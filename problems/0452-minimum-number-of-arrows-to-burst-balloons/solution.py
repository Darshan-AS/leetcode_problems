class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        return reduce(
            lambda a, x: (a[0] + 1, x[1]) if x[0] > a[1] else a,
            sorted(points, key=lambda p: p[1]),
            (0, -math.inf), # (shots_count, previous_end)
        )[0]
