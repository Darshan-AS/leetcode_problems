class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        
        i = 0
        while i < n:
            num = nums[i]
            if 1 <= num <= n and nums[num - 1] != num:
                nums[i], nums[num - 1] = nums[num - 1], nums[i]
            else:
                i += 1
        
        for i, x in enumerate(nums):
            if i + 1 != x:
                return i + 1
        return n + 1
            
