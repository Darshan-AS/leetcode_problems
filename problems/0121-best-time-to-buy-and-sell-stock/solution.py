class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        return max(map(sub, prices, accumulate(prices, min)))
