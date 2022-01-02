class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        # Copied to avoid study plan reset
        n = len(prices)
        if n < 2:
             return 0
        
        profit = 0
        minimum = prices[0]
        for i in range(1, n):
            if prices[i] < minimum:
                minimum = prices[i]
            elif prices[i] > minimum + fee:
                profit += prices[i] - fee - minimum
                minimum = prices[i] - fee
        
        return profit
