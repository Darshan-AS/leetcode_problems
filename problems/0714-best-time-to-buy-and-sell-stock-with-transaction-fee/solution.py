class Solution:
    def maxProfit(self, prices: list[int], fee: int) -> int:
        return reduce(lambda a, p: (max(a[0], a[1] - p), max(a[1], a[0] + p - fee)), prices, (-inf, 0))[1] # (hold, free)
