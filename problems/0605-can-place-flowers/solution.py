class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        a = 0
        for b, c in pairwise(chain(flowerbed, (0,))):
            k = a == b == c == 0
            a = 1 if k else b
            if n <= 0: return True
            n -= k
        return n <= 0
        
