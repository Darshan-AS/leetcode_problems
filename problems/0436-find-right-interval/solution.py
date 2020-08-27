from bisect import bisect_left

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        sorted_starts = sorted(map(lambda x: (x[1][0], x[0]), enumerate(intervals)))
        
        def get_right_interval(interval):
            start, end = interval
            index = bisect_left(sorted_starts, (end,))
            return sorted_starts[index][1] if index < len(sorted_starts) else -1
        
        return list(map(get_right_interval, intervals))
