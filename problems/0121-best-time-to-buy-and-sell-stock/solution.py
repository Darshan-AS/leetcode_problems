class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return max(map(operator.sub, prices, accumulate(prices, min)))
