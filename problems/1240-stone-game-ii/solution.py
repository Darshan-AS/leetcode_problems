class Solution:
    def stoneGameII(self, piles: list[int]) -> int:
        suffix_sums = tuple(reversed(tuple(accumulate(reversed(piles)))))

        @cache
        def score(i: int, m: int) -> int:
            return (i < len(piles)) and max(suffix_sums[i] - score(i + x, max(m, x)) for x in range(1, 2 * m + 1))
        
        return score(0, 1)
