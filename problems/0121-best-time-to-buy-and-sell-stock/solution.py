class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prefix_mins = accumulate(prices, min, initial=math.inf)
        return max(*starmap(operator.sub, zip(prices, prefix_mins)), 0)

