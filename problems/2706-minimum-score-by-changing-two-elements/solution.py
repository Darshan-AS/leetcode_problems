class Solution:
    def minimizeSum(self, nums: list[int]) -> int:
        s_nums = sorted(nums)
        return min(s_nums[i] - s_nums[j] for i, j in ((-1, 2), (-2, 1), (-3, 0)))
        
