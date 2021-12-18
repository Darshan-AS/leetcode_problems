from bisect import bisect_left

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        pass_days = [1, 7, 30]
        
        @cache
        def min_cost(day_index: int) -> int:
            return min(
                min_cost(bisect_left(days, days[day_index] + d, day_index)) + c
                for d, c in zip(pass_days, costs)
            ) if day_index < len(days) else 0
        
        return min_cost(0)
