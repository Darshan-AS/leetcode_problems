class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        global_max = current_max = nums[0]
        for i in nums[1:]:
            current_max = max(current_max + i, i)
            global_max = max(global_max, current_max)
        return global_max
