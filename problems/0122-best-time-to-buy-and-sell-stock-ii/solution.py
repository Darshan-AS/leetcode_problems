class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        prices.append(0)
        prices = [10000000000000] + prices
        for i in range(1, len(prices) - 1):
            if prices[i - 1] >= prices[i] and prices[i + 1] > prices[i]:
                profit -= prices[i]
            if prices[i - 1] < prices[i] and prices[i + 1] <= prices[i]:
                profit += prices[i]
        return profit
