from functools import reduce

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [0] * 366
        
        get_dp_at = lambda index: dp[index] if index >= 0 else 0
        days = set(days)
        
        for i in range(366):
            if i not in days:
                dp[i] = get_dp_at(i - 1)
                continue
                
            dp[i] = min(
                get_dp_at(i - 1) + costs[0],
                get_dp_at(i - 7) + costs[1],
                get_dp_at(i - 30) + costs[2]
            )
        
        return dp[-1]
