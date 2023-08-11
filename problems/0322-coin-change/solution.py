class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        @cache
        def count(a: int) -> int:
            return min(count(a - c) for c in coins) + 1 if a > 0 else inf if a else 0
        
        n = count(amount)
        return -1 if n == inf else n
