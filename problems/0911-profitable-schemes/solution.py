class Solution:
    def profitableSchemes(self, n_: int, min_profit: int, group: list[int], profit: list[int]) -> int:
        @cache
        def schemes(n: int, k: int, i: int) -> int:
            return (
                schemes(n, k, i + 1) +
                schemes(n - group[i], max(k - profit[i], 0), i + 1) +
                (n >= group[i] and k <= profit[i])
            ) % 1_000_000_007 if i < len(group) and n > 0 else 0
        
        return (schemes(n_, min_profit, 0) + (min_profit == 0)) % 1_000_000_007
        
