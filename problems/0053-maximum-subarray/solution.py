from itertools import accumulate

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        return max(accumulate(nums, lambda max_, num: max(max_ + num, num)))
