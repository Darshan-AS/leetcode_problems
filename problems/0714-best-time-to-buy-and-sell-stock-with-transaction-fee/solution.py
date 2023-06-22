class Solution:
    def maxProfit(self, prices: list[int], fee: int) -> int:
        @cache
        def max_profit(i: int) -> int:
            if i < 0: return (-inf, 0)
            hold, free = max_profit(i - 1)
            return max(hold, free - prices[i]), max(free, hold + prices[i] - fee)
        
        return max_profit(len(prices) - 1)[1]
