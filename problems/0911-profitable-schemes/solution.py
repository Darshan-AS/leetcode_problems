class Solution:
    def profitableSchemes(self, n_: int, min_profit: int, group: list[int], profit: list[int]) -> int:
        @cache
        def schemes(n: int, k: int, i: int) -> int:
            return (
                schemes(n, k, i + 1) +
                schemes(n - group[i], max(k - profit[i], 0), i + 1)
            ) % 1_000_000_007 if i < len(group) and n >= 0 else n >= 0 and k == 0

        return schemes(n_, min_profit, 0)
