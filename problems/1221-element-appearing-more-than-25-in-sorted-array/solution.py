class Solution:
    def findSpecialInteger(self, arr: list[int]) -> int:
        return next(x for x, g in groupby(arr) if sum(1 for _ in g) > len(arr) / 4)
        
