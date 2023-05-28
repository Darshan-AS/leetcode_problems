class Solution:
    def minCost(self, n: int, cuts: list[int]) -> int:
        s_cuts = sorted(chain(cuts, (0, n)))

        @cache
        def min_cost(i: int, j: int) -> int:
            return (cost := s_cuts[j] - s_cuts[i]) + min((min_cost(i, k) + min_cost(k, j) for k in range(i + 1, j)), default=-cost)
        
        return min_cost(0, len(s_cuts) - 1)
