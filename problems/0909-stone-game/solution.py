from functools import lru_cache

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        @lru_cache(maxsize=None)
        def maximize(i, j):
            if i >= j:
                return piles[i]

            return max(
                piles[i] - minimize(i + 1, j),
                piles[j] - minimize(i, j - 1),
            )

        @lru_cache(maxsize=None)
        def minimize(i, j):
            if i >= j:
                return piles[i]

            return min(
                piles[i] - maximize(i + 1, j),
                piles[j] - maximize(i, j - 1),
            )

        return bool(maximize(0, len(piles) - 1))
        
        
    
