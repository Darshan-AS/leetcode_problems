class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        walker = 0
        for runner in range(len(nums)):
            if nums[walker] != nums[runner]:
                walker += 1
                nums[walker] = nums[runner]
        
        return walker + 1
