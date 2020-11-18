class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        def merge_helper(sorted_intervals):
            prev = sorted_intervals[0]
            for curr in sorted_intervals[1:]:
                if curr[0] > prev[1]:
                    yield prev
                    prev = curr
                else:
                    prev = min(prev[0], curr[0]), max(prev[1], curr[1])
            else:
                yield prev
        
        intervals.sort()
        return list(merge_helper(intervals))
