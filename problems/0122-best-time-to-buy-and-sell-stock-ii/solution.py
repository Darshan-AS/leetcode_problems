class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        return sum(max(b - a, 0) for a, b in pairwise(prices))
