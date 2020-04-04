class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i = 0
        for j in range(len(nums)):
            if nums[j]:
                temp = nums[j]
                nums[j] = 0
                nums[i] = temp
                i += 1
        
