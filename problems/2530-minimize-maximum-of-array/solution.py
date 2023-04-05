class Solution:
    def minimizeArrayValue(self, nums: list[int]) -> int:
        return max(ceil(x / i) for i, x in enumerate(accumulate(nums), 1))

