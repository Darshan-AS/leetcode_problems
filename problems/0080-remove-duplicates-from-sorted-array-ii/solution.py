class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 2
        
        walker = 0
        for runner in range(len(nums)):
            if walker < k or nums[runner] != nums[walker - k]:
                nums[walker] = nums[runner]
                walker += 1
        
        return walker
