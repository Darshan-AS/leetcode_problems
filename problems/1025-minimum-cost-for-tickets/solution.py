from functools import reduce
from bisect import bisect_left

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:        
        @lru_cache
        def dp(index):
            if index >= len(days): return 0
            day = days[index]
            return min(dp(bisect_left(days, day + d)) + c for d, c in zip((1, 7, 30), costs))
        
        return dp(0)
