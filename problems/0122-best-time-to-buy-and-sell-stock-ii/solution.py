class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        min_val = max_val = prices[0]
        profit = 0
        for i in prices:
            if i > max_val:
                max_val = i
                
            if i < max_val:
                profit += max_val - min_val
                min_val = max_val = i
              
        profit += max_val - min_val
        return profit

    
