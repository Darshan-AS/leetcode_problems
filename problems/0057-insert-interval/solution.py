class Solution:
    def insert(self, intervals: list[list[int]], new_interval: list[int]) -> list[list[int]]:
        si = bisect.bisect_left( intervals, new_interval[0], key=lambda x: x[1])
        ei = bisect.bisect_right(intervals, new_interval[1], key=lambda x: x[0])
        
        start = min(intervals[si][0], new_interval[0]) if si < len(intervals) else new_interval[0]
        end = max(intervals[ei - 1][1], new_interval[1]) if ei > 0 else new_interval[1]

        return intervals[:si] + [[start, end]] + intervals[ei:]

