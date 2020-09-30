class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if not nums: return 1
        
        n = len(nums)
        for i in range(n):
            j = nums[i]
            while (j is not None) and 0 < j <= n:
                nums[j - 1], j = None, nums[j - 1]
        
        for i in range(n):
            if nums[i] is not None:
                return i + 1
        return n + 1
