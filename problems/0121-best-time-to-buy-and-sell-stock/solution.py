class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        if not prices: return profit
        
        min_price = prices[0]
        for curr_price in prices:
            profit = max(profit, curr_price - min_price)
            min_price = min(min_price, curr_price)
        return profit
