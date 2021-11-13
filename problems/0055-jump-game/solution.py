class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_index = 0
        i = 0
        while i <= max_index < len(nums):
            max_index = max(max_index, i + nums[i])
            i += 1
        return max_index >= len(nums) - 1
