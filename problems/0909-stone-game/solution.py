class Solution:
    def stoneGame(self, piles: list[int]) -> bool:
        @cache
        def score(i: int, j: int) -> int:
            return (i < j) and max(piles[i] + score(i + 1, j), piles[j] + score(i, j - 1))
        
        return score(0, len(piles) - 1)
