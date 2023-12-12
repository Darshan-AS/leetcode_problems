class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        m1, m2 = reduce(lambda a, x: (x, a[0]) if x > a[0] else ((a[0], x) if x > a[1] else a), nums, (0, 0))
        return (m1 - 1) * (m2 - 1)
