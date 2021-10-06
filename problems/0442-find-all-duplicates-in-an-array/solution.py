class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        dups = []
        for x in nums:
            i = abs(x) - 1
            if nums[i] < 0: dups.append(abs(x))
            nums[i] *= -1
        
        # Fix input array
        for i, x in enumerate(nums):
            if x < 0: nums[i] *= - 1
        
        return dups
