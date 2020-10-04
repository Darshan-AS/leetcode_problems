from itertools import product

class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        count = len(intervals)
        for a, b in intervals:
            for c, d in intervals:
                if c <= a and b <= d and not (a == c and b == d):
                    count -= 1
                    break
        
        return count
