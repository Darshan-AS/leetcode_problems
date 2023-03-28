class Solution:
    def mincostTickets(self, days: list[int], costs: list[int]) -> int:
        dp = [0] * (len(days) + 1)
        for i, x in enumerate(days):
            dp[i + 1] = min(
                dp[bisect.bisect(days, x - d, 0, i)] + c
                for d, c in zip((1, 7, 30), costs)
            )
        return dp[-1]
