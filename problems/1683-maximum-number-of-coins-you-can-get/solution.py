class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        return sum(map(sorted(piles).__getitem__, range(len(piles) // 3, len(piles), 2)))
