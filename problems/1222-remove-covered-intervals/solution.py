from itertools import product

class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        sorted_intervals = sorted(intervals, key=lambda x: (x[0], -x[1]))
        count = len(intervals)
        right = -1
        for _, b in sorted_intervals:
            if b <= right: count -=1
            else: right = b
        return count
