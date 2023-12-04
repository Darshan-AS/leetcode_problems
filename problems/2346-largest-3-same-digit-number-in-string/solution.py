class Solution:
    def largestGoodInteger(self, num: str) -> str:
        return max((x for x, g in groupby(num) if sum(1 for _ in g) >= 3), default='') * 3
