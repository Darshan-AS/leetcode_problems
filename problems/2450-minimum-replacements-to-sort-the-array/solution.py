class Solution:
    def minimumReplacement(self, nums: list[int]) -> int:
        return reduce(lambda a, x: (x, a[1]) if x <= a[0] else (x // (z := ceil(x / a[0])), a[1] + z - 1), reversed(nums), (inf, 0))[-1]
