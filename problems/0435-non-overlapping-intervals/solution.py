class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:        

        def pick_or_delete(a, x):
            prev_end, deleted = a
            start, end = x
            return (prev_end, deleted + 1) if start < prev_end else (end, deleted)
    
        s_intervals = sorted(intervals, key=lambda x: x[1])
        return reduce(pick_or_delete, s_intervals, (-math.inf, 0))[1]
