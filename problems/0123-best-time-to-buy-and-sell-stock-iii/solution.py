class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        n = len(prices)
        
        min_ = prices[0]
        left = [0] * n
        for i in range(1, n):
            min_ = min(min_, prices[i])
            left[i] = max(left[i - 1], prices[i] - min_)
        
        max_ = prices[-1]
        right = [0] * n
        for i in range(n - 2, -1, -1):
            max_ = max(max_, prices[i])
            right[i] = max(right[i + 1], max_ - prices[i])
        
        return max(map(lambda x: x[0] + x[1], zip(left, right)))
