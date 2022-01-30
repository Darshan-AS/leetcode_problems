class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i, j, n = 0, 0, len(nums)
        
        while i <= j < n - 1:
            i, j = i + 1, max(j, i + nums[i])
        
        return j >= n - 1
