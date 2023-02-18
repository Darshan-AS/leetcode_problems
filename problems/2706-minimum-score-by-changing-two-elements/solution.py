class Solution:
    def minimizeSum(self, nums: list[int]) -> int:
        s_nums = sorted(nums)
        k = 2
        return min(
            s_nums[i] - s_nums[j]
            for i, j in zip(range(-1, -k - 2, -1), range(k, -1, -1))
        )
        
