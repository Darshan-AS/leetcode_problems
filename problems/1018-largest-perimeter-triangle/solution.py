class Solution:
    def largestPerimeter(self, nums: list[int]) -> int:
        s_nums = sorted(nums, reverse=True)
        
        for i in range(len(nums) - 2):
            if s_nums[i] < s_nums[i + 1] + s_nums[i + 2]:
                return sum(s_nums[i: i + 3])
        return 0
