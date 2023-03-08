class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        l, r = 1, max(piles)
        while l < r:
            k = (l + r) // 2
            hours = sum(ceil(n / k) for n in piles)
            l, r = (l, k) if hours <= h else (k + 1, r)
        return l
