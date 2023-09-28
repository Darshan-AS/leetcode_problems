class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        i, j = 0, len(nums) - 1
        while i < j:
            if nums[i] % 2:
                nums[j], nums[i] = nums[i], nums[j]
                j -= 1
            else:
                i += 1
        return nums
        
