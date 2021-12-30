class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def pairwise(iterable):
            a, b = tee(iterable)
            next(b, None)
            return zip(a, b)
        
        return sum(filter(lambda p: p > 0, (sp - cp for cp, sp in pairwise(prices))))
