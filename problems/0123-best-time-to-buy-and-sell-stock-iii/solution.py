class Solution:
    def maxProfit(self, prices: List[int]) -> int:   
        prefix_mins = accumulate(prices, min)
        suffix_maxes = accumulate(reversed(prices), max)
        
        prefix_profits = map(sub, prices, prefix_mins)
        suffix_profits = map(sub, suffix_maxes, reversed(prices))
        
        max_prefix_profits = list(accumulate(prefix_profits, max))
        max_suffix_profits = list(accumulate(suffix_profits, max))
        
        return max(map(add, max_prefix_profits, reversed(max_suffix_profits)))
