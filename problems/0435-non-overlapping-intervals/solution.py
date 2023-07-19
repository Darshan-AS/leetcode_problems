class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        return reduce(
            lambda a, x:  (x[1], a[1]) if a[0] <= x[0] else (a[0], a[1] + 1),
            sorted(intervals, key=itemgetter(1)),
            (-inf, 0), # (previous_end, removed_count)
        )[1]

