class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        
        res = intervals[0]
        for interval in intervals:
            if interval[0] <= res[1]:
                res = [res[0], max(res[1], interval[1])]
            else:
                yield res
                res = interval
        yield res
        
