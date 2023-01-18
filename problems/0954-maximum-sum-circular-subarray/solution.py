class Solution:
    def maxSubarraySumCircular(self, nums: list[int]) -> int:
        max_sum = max(accumulate(nums, lambda a, x: max(a, 0) + x))
        min_sum = min(accumulate(nums, lambda a, x: min(a, 0) + x))
        
        single_interval_max = max_sum
        double_interval_max = sum(nums) - min_sum

        return max(single_interval_max, double_interval_max) if double_interval_max else single_interval_max
