class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Copied to avoid study plan reset
        sold = 0
        hold = -math.inf
        cool = 0
        for price in prices:
            sold_tmp = sold
            sold = max(sold, hold + price)
            hold = max(hold, cool - price)
            cool = sold_tmp
        return sold
