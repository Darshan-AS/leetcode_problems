class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i = 0
        for j in range(len(nums)):
            if nums[j]:
                nums[i],  nums[j] = nums[j], nums[i]
                i += 1
