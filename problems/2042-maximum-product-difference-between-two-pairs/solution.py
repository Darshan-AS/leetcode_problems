class Solution:
    def maxProductDifference(self, nums: list[int]) -> int:
        a, b = reduce(lambda a, x: (x, a[0]) if x > a[0] else (a[0], max(a[1], x)), nums, (-inf, -inf))
        c, d = reduce(lambda a, x: (x, a[0]) if x < a[0] else (a[0], min(a[1], x)), nums, (+inf, +inf))
        return a * b - c * d

