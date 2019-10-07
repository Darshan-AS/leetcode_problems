class Solution:
            
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        min_val = max_val = prices[0]
        profit = 0
        for i in prices:
            if i < min_val:
                min_val = i
             
            max_val = i      
            profit = max(profit, max_val - min_val)
            
        return profit
