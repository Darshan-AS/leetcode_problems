class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        return max(chain(
            accumulate(nums, lambda a, x: max(a + x, x)),
            map(abs, accumulate(nums, lambda a, x: min(a + x, x)))
        ))
