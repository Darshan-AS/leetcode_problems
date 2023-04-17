class Solution:
    def kidsWithCandies(self, candies: list[int], k: int) -> list[bool]:
        return list(map(ge, map(add, candies, repeat(k)), repeat(max(candies))))
