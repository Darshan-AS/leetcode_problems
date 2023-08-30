class Solution:
    def minimumReplacement(self, nums: list[int]) -> int:
        return reduce(lambda a, x: (a[0], x) if x <= a[1] else (a[0] + (z := ceil(x / a[1])) - 1, x // z), reversed(nums), (0, inf))[0]
