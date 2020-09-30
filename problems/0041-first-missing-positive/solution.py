class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if not nums: return 1
        
        n = len(nums)
        for i in range(n):
            j = nums[i]
            while 0 < j <= n and nums[j - 1] != j:
                nums[j - 1], j = j, nums[j - 1]
        
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1
