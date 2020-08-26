from functools import reduce

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        days = set(days)
        
        @lru_cache
        def dp(i):
            if i < 0: return 0
            return min(dp(i - d) + c for d, c in zip((1, 7, 30), costs)) if i in days else dp(i - 1)  
        return dp(365)
